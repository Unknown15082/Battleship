import sys
sys.path.append('../')

from Battleship.Files.Battleship import *
import unittest

class TestShipBoard(unittest.TestCase):
    def setUp(self):
        self.sboard = ShipBoard()

    def test_squares(self):
        self.assertEqual(len(self.sboard.squares), 100)

    def test_remain(self):
        k = []
        for _ in range(100): k.append(False)
        self.assertEqual(self.sboard.remain, k)


class TestAtkBoard(unittest.TestCase):
    def setUp(self):
        self.aboard = AtkBoard()

    def test_squares(self):
        self.assertEqual(len(self.aboard.squares), 100)

    def test_legal(self):
        k = []
        for _ in range(100): k.append(True)
        self.assertEqual(self.aboard.legal, k)
    
class TestSquare1(unittest.TestCase):
    def setUp(self):
        self.sq = Square(1, 2, "ship")

    def test_row(self):
        self.assertEqual(self.sq.row, 1)
    
    def test_column(self):
        self.assertEqual(self.sq.col, 2)

    def test_state(self):
        self.assertTrue(self.sq.state)

    def test_type(self):
        self.assertEqual(self.sq.type, "ship")

    def test_cont(self):
        self.assertEqual(self.sq.content, "-")

    def test_color(self):
        self.assertEqual(self.sq.color, "#ffffff")

if __name__ == "__main__":
    unittest.main()