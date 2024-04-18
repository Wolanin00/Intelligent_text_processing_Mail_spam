.DEFAULT_GOAL := all

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: format
format:
	black .
	ruff check . --fix --exit-zero

.PHONY: unit_test
unit_test:
	pytest tests\unit_tests

.PHONY: integration_test
integration_test:
	pytest tests\integration_tests


