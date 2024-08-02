default: help

TGT = dotfile_mgr
APP = $(TGT).py
VENV = .venv
VBIN = $(VENV)/bin
PYTEST = $(VBIN)/pytest

help:
	@echo "clean -- remove files not needed"
	@echo "pytest -- run all unit tests"
	@echo "coverage -- pytest coverage"
	@echo "$(TGT) -- run the manager"

# The app does not need a virtual environment.
# But the unit tests take advantage of pytest.
$(VENV):
	python3 -m venv $(VENV) && $(VBIN)/pip3 install pytest pytest-cov

pytest: .venv
	$(PYTEST) $(APP)

coverage: .venv
	$(PYTEST) --cov=. --cov-report=html --cov-report=term-missing $(APP)
	$(VBIN)/python3 -m webbrowser "file://$(PWD)/htmlcov/index.html"


clean:
	rm -rf .coverage* .pytest_cache __pycache__ htmlcov $(VENV)

$(TGT):
	./$(APP)

.PHONY: pytest coverage clean default $(TGT)
.NOTPARALLEL: $(VENV) clean
