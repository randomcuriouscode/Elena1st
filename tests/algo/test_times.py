import unittest
import timeit
from elena.parse.parser import parse

nodeStorage = parse("/Users/avaneesh/amherst")


class TestTimes(unittest.TestCase):
    setup = '''
from elena.algo import yen_paths
from elena.algo import lawler_paths
from tests.algo.test_times import nodeStorage

'''

    def test_time(self):
        print (min(timeit.Timer('yen_paths.get_shortest_paths(nodeStorage, 66677654, 61791707, 120)',
                                setup=self.setup).repeat(5, 100)))
        print (min(timeit.Timer('lawler_paths.get_shortest_paths(nodeStorage, 66677654, 61791707, 120)',
                                setup=self.setup).repeat(5, 100)))


if __name__ == '__main__':
    unittest.main()
