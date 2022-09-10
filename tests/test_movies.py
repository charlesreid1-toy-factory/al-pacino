import os
import sys
import unittest

from al_pacino.movies import Movie, Gf, Gf2, Gf3, Serpico, Scarface, Ggr, Heat

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

from tests import utils


class TestMovies(unittest.TestCase):
    def test_movies(self):
        # base class
        with self.assertRaises(NotImplementedError):
            Movie().get_title()

        # child classes
        correct = [
            (Gf, "The Godfather"),
            (Gf2, "The Godfather Part II"),
            (Gf3, "The Godfather Part III"),
            (Serpico, "Serpico"),
            (Scarface, "Scarface"),
            (Ggr, "Glengarry Glen Ross"),
            (Heat, "Heat"),
        ]
        for cls, correct_title in correct:
            with utils.CaptureStdout() as output:
                cls().get_title()
            self.assertIn(correct_title, output[0])


if __name__ == "__main__":
    unittest.main()
