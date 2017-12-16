import unittest

from fullstack.server.elena.algo import yen_paths
from fullstack.server.elena.algo import lawler_paths
from fullstack.server.elena.parse.parser import parse
from fullstack.server.elena.util.util import calculate_cost
from fullstack.server.elena.algo.shortest_path import *


class TestPaths(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodeStorage = parse("srtm_prod.osm")

    def test_calculate_cost(self):
        path = [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66701422, 66710693, 66709586, 66727122,
                66689101, 66604339, 61793182, 61791707]
        dist = calculate_cost(self.nodeStorage, path)
        self.assertAlmostEqual(dist, 197.02832391036094, 5)

    def test_a_star(self):
        path, cost = get_a_star_path(self.nodeStorage, 61791707, 66604339)
        self.assertEqual([61791707, 61793182, 66604339], path)

    def test_yen(self):
        A = yen_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        self.assertEqual([([66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66623818, 66666937, 66745352,
                            66661092, 66662354, 61793182, 61791707], 184.49243890233382), (
                              [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66623818, 66710693, 66709586,
                               66727122, 66689101, 66604339, 61793182, 61791707], 195.83627985922084), (
                              [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66701422, 66710693, 66709586,
                               66727122, 66689101, 66604339, 61793182, 61791707], 197.028323910472), (
                              [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66701422, 66710693, 66623818,
                               66666937, 66745352, 66661092, 66662354, 61793182, 61791707], 208.6237810829519)], A)

    def test_lawler(self):
        A = lawler_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        self.assertEqual([([66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66623818, 66666937, 66745352,
                            66661092, 66662354, 61793182, 61791707], 184.49243890233382), (
                          [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66623818, 66710693, 66709586,
                           66727122, 66689101, 66604339, 61793182, 61791707], 195.83627985922084), (
                          [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66701422, 66710693, 66709586,
                           66727122, 66689101, 66604339, 61793182, 61791707], 197.028323910472), (
                          [66677654, 66754238, 66711385, 66732536, 66718935, 66769489, 66701422, 66710693, 66623818,
                           66666937, 66745352, 66661092, 66662354, 61793182, 61791707], 208.6237810829519)], A)

    def test_yen_lawler(self):
        A = yen_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        B = lawler_paths.get_shortest_paths(self.nodeStorage, 66677654, 61791707, 120)
        self.assertEqual(A, B)


if __name__ == '__main__':
    unittest.main()
