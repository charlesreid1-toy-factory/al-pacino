import os
import sys
import unittest

from al_pacino.animals import Animal, Goat, Cow, Pig, Dog, Cat, Human

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from tests import utils


class TestAnimals(unittest.TestCase):
    def test_make_noise(self):
        # base class
        with self.assertRaises(NotImplementedError):
            Animal().make_noise()

        # child classes
        correct = [
            (Goat, "baaa"),
            (Cow, "moo"),
            (Pig, "oink"),
            (Dog, "arf"),
            (Cat, "mrkgnao"),
            (Human, "buuurp"),
        ]
        for cls, correct_noise in correct:
            with utils.CaptureStdout() as output:
                cls().make_noise()
            self.assertIn(correct_noise, "".join(output))


if __name__ == "__main__":
    unittest.main()
