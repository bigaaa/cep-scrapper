.DEFAULT_GOAL := default_target

PYTEST := py.test

PROJECT_NAME := cep-scrapper
PYTHON_VERSION := 3.8.5
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

install-dependencies:
	pip3 install -r requirements.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv install-dependencies

test:
	pytest tests/tests.py -v

default_target: test