# al-pacino

<img alt="version-0.1.0" src="https://img.shields.io/badge/version-0.1.0-orange" />

<img 
alt="tests-unittest" src="https://img.shields.io/badge/tests-unittest-green" /><img 
alt="tests-coverage" src="https://img.shields.io/badge/tests-coverage-green" />

<img
alt="codestyle-black" src="https://img.shields.io/badge/codestyle-black-%23222222" /><img 
alt="codestyle-flake8" src="https://img.shields.io/badge/codestyle-flake8-blue" />

<img alt="python-3.7-3.8-3.9-3.10" src="https://img.shields.io/badge/python-3.7%7C3.8%7C3.9%7C3.10-blue" />

![Al Pacino](docs/img/pacino.jpg)

A package that demonstrates how to add tests using unittest
and coverage, and how to separately run core tests (tests of
the core library functionality) and utility tests (tests of the
supporting test utility functions and test infrastructure that
do not use the core library itself.)

## Quick Start

Start by cloning the repo:

```
git clone git@github.com:charlesreid1-toy-factory/al-pacino.git
cd al-pacino
```

Before you begin, create an `environment` file so you can use the Makefile:

```
cp environment.example environment
```

Update the environment file to point to the repository location on disk.

Now you can set up a virtual environment, and install the required packages
and then the `al_pacino` library into it:

```
python3 -m virtualenv vp && source vp/bin/activate
python3 -m pip install -r requirements.txt
make clean
make build
```

Now you can use the library like so:

```
$ python3

>>> from al_pacino.animals import Cow
>>> print(Cow().speak())
moo
```

Now you're off and running.

## Running Tests

To run tests, start by installing the test dependencies:

```
python3 -m pip install -r requirements-test.txt
python3 setup.py build install
```

Now run tests:

```
# Only run tests of test utilities and test support infrastructure
make utility_test

# Only run tests of the core Al Pacino library
make pacino_test

# Run all tests
make test
```

The utility test suite will not report any coverage, but the pacino test suite will:

```
$ make pacino_test
/Library/Developer/CommandLineTools/usr/bin/make -j1 tests/test_animals.py
flake8 src tests
coverage run -p --source=al_pacino tests/test_animals.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
/Library/Developer/CommandLineTools/usr/bin/make coverage
coverage combine
Combined data file .coverage.aptos.32308.349086
coverage report
Name                                                                             Stmts   Miss  Cover
----------------------------------------------------------------------------------------------------
vp/lib/python3.9/site-packages/al_pacino-0.1.0-py3.9.egg/al_pacino/__init__.py       1      0   100%
vp/lib/python3.9/site-packages/al_pacino-0.1.0-py3.9.egg/al_pacino/animals.py       18      0   100%
----------------------------------------------------------------------------------------------------
TOTAL                                                                               19      0   100%
```
