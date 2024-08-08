default: help

TGT = dotfile_mgr
APP = $(TGT).py
VENV = build/.venv
VBIN = $(VENV)/bin
PYTEST = $(VBIN)/pytest -o cache_dir=build/.pytest_cache

# Or: PYTHONPYCACHEPREFIX=build/__pycache__
export PYTHONDONTWRITEBYTECODE = 1

help:
	@echo "Targets for $(TGT):"
	@echo "clean -- remove files not needed"
	@echo "pytest -- run all unit tests"
	@echo "coverage -- pytest coverage"
	@echo "$(TGT) -- run the manager"

# The app does not need a virtual environment.
# But the unit tests take advantage of pytest.
$(VENV):
	python3 -m venv $(VENV) && $(VBIN)/pip3 install --upgrade pip pytest pytest-cov

pytest: $(VENV)
	$(PYTEST) $(APP)

coverage: $(VENV)
	$(PYTEST) --cov=. --cov-report=html --cov-report=term-missing $(APP)
	$(VBIN)/python3 -m webbrowser "file://$(PWD)/htmlcov/index.html"


clean:
	rm -rf build .coverage* __pycache__ htmlcov

$(TGT):
	./$(APP)

.PHONY: pytest coverage clean default $(TGT)
.NOTPARALLEL: $(VENV) clean
