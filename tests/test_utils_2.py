import sys
import os
import unittest

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from tests import utils


class TestGreenLight(unittest.TestCase):
    def test_simple(self):
        a = 1+1
        b = 2
        self.assertEqual(a, b)

    def test_random(self):
        a = 1+1
        r = utils.random_alphanumeric_string(N=2)
        b = len(r)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
