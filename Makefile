.DEFAULT_GOAL := all

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: flask_app
flask_app:
	python flask_app.py

.PHONY: tkinter_app
tkinter_app:
	python tkinter_app.py

.PHONY: format
format:
	black .
	ruff check . --fix --exit-zero

.PHONY: test
test:
	pytest tests

.PHONY: unit_test
unit_test:
	pytest tests\unit_tests

.PHONY: integration_test
integration_test:
	pytest tests\integration_tests


