import unittest
from elena.yen_paths import *
from elena.parse import *


class TestPaths(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodeStorage = parse("/Users/avaneesh/amherst")

    def test_a_star(self):
        path, cost = get_a_star_path(self.nodeStorage, 61791707, 66604339)
        print("Path = {}".format(path))
        print("Cost = {}".format(cost))


if __name__ == '__main__':
    unittest.main()
