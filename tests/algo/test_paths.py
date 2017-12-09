import unittest

from elena.algo import yen_paths
from elena.algo import lawler_paths
from elena.parse.parser import parse
from elena.util.util import calculate_cost
from elena.algo.shortest_path import *


class TestPaths(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodeStorage = parse("/Users/avaneesh/amherst")

    def test_calculate_cost(self):
        path = [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66701422, 66710693, 66709586, 66727122, 66689101, 66604339, 61793182, 61791707]
        dist = calculate_cost(self.nodeStorage, path)
        print(dist)

    def test_a_star(self):
        path, cost = get_a_star_path(self.nodeStorage, 61791707, 66604339)
        self.assertEqual([61791707, 61793182, 66604339], path)

    def test_yen(self):
        A = yen_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        print(A)

    def test_lawler(self):
        A = lawler_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        print(A)

    def test_yen_lawler(self):
        A = yen_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        B = lawler_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        self.assertEqual(A, B)


if __name__ == '__main__':
    unittest.main()
