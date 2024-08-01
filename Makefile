default: help

APP = dotfile_mgr.py
VENV = .venv
VBIN = $(VENV)/bin
PYTEST = $(VBIN)/pytest

help:
	echo help

# The app does not need a virtual environment.
# But the unit tests take advantage of pytest.
$(VENV):
	python3 -m venv $(VENV) && $(VBIN)/pip3 install pytest pytest-cov

pytest: .venv
	$(PYTEST) $(APP)

coverage: .venv
	$(PYTEST) --cov=. --cov-report=term-missing $(APP)

clean:
	rm -rf .coverage* .pytest_cache __pycache__ $(VENV)
