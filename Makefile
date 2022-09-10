include common.mk
MODULES=tests

all: build test

lint:
	flake8 $(MODULES)

build:
	python3 setup.py build install

# Vars
# 
tests:=$(wildcard tests/test_*.py)

# Run standalone tests 
# 
test:
	$(MAKE) -j1 $(tests)

# A pattern rule that runs a single test script
#
$(tests): %.py : lint
	python -m unittest $*.py
	#coverage run -p --source=src $*.py
	#coverage combine
	#coverage report

# Run standalone and integration tests
#
all_test:
	$(MAKE) AL_PACINO_TEST_MODE="standalone integration" test

# Run integration tests only
#
integration_test:
	$(MAKE) AL_PACINO_TEST_MODE="integration" test

.PHONY: all lint build test all_test integration_test $(tests)
