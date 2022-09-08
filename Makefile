include common.mk
MODULES=tests

all: test

lint:
	flake8 $(MODULES)

########################################
# Vars
# 
tests:=$(wildcard tests/test_*.py)

serial_tests:=tests/test_found.py \
              tests/test_graph.py \
              tests/test_stars.py

parallel_tests:=$(filter-out $(serial_tests),$(tests))

########################################
# Run standalone tests 
# 
serial_test:
	$(MAKE) -j1 $(serial_tests)

parallel_test:
	$(MAKE) -j4 $(parallel_tests)

########################################
# A pattern rule that runs a single test script
#
$(tests): %.py : lint
	coverage run -p --source=src $*.py

# Run standalone and integration tests
#
all_test:
	$(MAKE) AL_PACINO_TEST_MODE="standalone integration" test

########################################
# Run integration tests only
#
integration_test:
	$(MAKE) AL_PACINO_TEST_MODE="integration" test

smoketest:
	$(MAKE) AL_PACINO_TEST_MODE="integration" tests/test_smoketest.py

.PHONY: all lint test safe_test serial_test all_test integration_test smoketest $(tests)
