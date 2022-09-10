import os
import unittest


def utility(f):
    return unittest.skipUnless(is_utility(), "Skipping utility test")(f)


def is_utility():
    return "utility" in _test_mode()


def pacino(f):
    return unittest.skipUnless(is_pacino(), "Skipping pacino test")(f)


def is_pacino():
    return "pacino" in _test_mode()


def always(f):
    return f


def _test_mode():
    return os.environ.get('AL_PACINO_TEST_MODE', "pacino")
