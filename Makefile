include common.mk
MODULES=tests

all: test

lint:
	flake8 $(MODULES)

########################################
# Vars
# 
tests:=$(wildcard tests/test_*.py)

########################################
# Run standalone tests 
# 
test:
	$(MAKE) -j1 $(tests)

parallel_test:
	$(MAKE) -j4 $(tests)

########################################
# A pattern rule that runs a single test script
#
$(tests): %.py : lint
	coverage run -p --source=src $*.py

# Run standalone and integration tests
#
all_test:
	$(MAKE) AL_PACINO_TEST_MODE="standalone integration" test

# Run integration tests only
#
integration_test:
	$(MAKE) AL_PACINO_TEST_MODE="integration" test

.PHONY: all lint test safe_test all_test integration_test $(tests)
