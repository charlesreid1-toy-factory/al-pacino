import os
import sys
import json
import unittest

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from tests import utils


class TestCaptureStdout(unittest.TestCase):
    def test_capture(self):
        # generate content
        content = []
        for _ in range(10):
            content.append(utils.random_alphanumeric_string())
        # print content and capture
        with utils.CaptureStdout() as capture:
            for c in content:
                print(c)
        # check content
        self.assertEqual(len(capture), len(content))
        for c in content:
            self.assertIn(c, capture)


if __name__ == "__main__":
    unittest.main()
