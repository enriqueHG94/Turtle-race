import unittest
from main import colors, y_positions, all_turtles, is_race_on


class TestRace(unittest.TestCase):

    def test_colors(self):
        self.assertEqual(len(colors), 6)

    def test_positions(self):
        self.assertEqual(len(y_positions), 6)

    def test_turtles(self):
        self.assertEqual(len(all_turtles), 6)

    def test_race_status(self):
        self.assertEqual(is_race_on, False)


if __name__ == '__main__':
    unittest.main()
