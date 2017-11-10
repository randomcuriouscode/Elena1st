import unittest
from elena.parse import *


class TestParsing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodeStorage = parse("/Users/avaneesh/amherst")

    def test_parseCheck(self):
        self.assertEqual(len(self.nodeStorage.nodeMap), 45071)

    def test_get_distance(self):
        dist = get_distance(self.nodeStorage.get_node(61793182), self.nodeStorage.get_node(66604339))
        self.assertAlmostEqual(5.946650009791097, dist, 5)


if __name__ == '__main__':
    unittest.main()
