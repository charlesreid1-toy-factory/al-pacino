include common.mk
MODULES=src tests

all: build test

lint:
	flake8 $(MODULES)

build:
	python3 setup.py build install

# Vars
# - one for all tests
# - one for pacino tests, testing the core library
# - one for utility tests, not testing core library
# 
tests:=$(wildcard tests/test_*.py)
utility_tests:=tests/test_utils.py \
			   tests/test_utils_2.py
pacino_tests:=$(filter-out $(utility_tests),$(tests))

# Run utility tests
#
utility_test:
	$(MAKE) -j1 $(utility_tests)

# Run pacino tests
#
pacino_test:
	$(MAKE) -j1 $(pacino_tests)
	$(MAKE) coverage

# Pattern rule to match a single test script
# Utility tests are run directly via python -m unittest
# Pacino tests are run via coverage
#
$(utility_tests): %.py : lint
	python -m unittest $*.py

$(pacino_tests): %.py : lint
	coverage run -p --source=al_pacino $*.py

# Report coverage info
# 
coverage:
	coverage combine
	coverage report

# Run utility and pacino tests both
#
test:
	$(MAKE) utility_test
	$(MAKE) pacino_test

# Clean
#
clean: clean-build clean-pyc clean-test ## remove all build, test, and Python artifacts

clean-build:
	@rm -fr build/ dist/ .eggs *.egg*

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -f .coverage*

.PHONY: all lint build utility_test pacino_test coverage test $(tests)
