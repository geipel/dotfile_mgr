default: help

help:
	echo help

# The app does not need a virtual environment.
# But the unit tests take advantage of pytest.
.venv:
	python3 -m venv .venv && .venv/bin/pip3 install pytest pytest-cov

PYTEST = .venv/bin/pytest

pytest: .venv
	$(PYTEST) dotfile_mgr.py

coverage: .venv
	$(PYTEST) --cov=. --cov-report=term-missing dotfile_mgr.py
