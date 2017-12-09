import unittest
import timeit
from elena.parse.parser import parse
import random

nodeStorage = parse("/Users/avaneesh/amherst")
key_list = list(nodeStorage.nodeMap.keys())
node1 = random.choice(key_list)
node2 = random.choice(key_list)


class TestTimes(unittest.TestCase):
    setup = '''
from elena.algo import yen_paths
from elena.algo import lawler_paths
from tests.algo.test_times import nodeStorage, node1, node2

print(node1)
print(node2)
'''

    def test_time(self):
        print (min(timeit.Timer('yen_paths.get_shortest_paths(nodeStorage, node1, node2, 120)',
                                setup=self.setup).repeat(3, 100)))
        print (min(timeit.Timer('lawler_paths.get_shortest_paths(nodeStorage, node1, node2, 120)',
                                setup=self.setup).repeat(3, 100)))


if __name__ == '__main__':
    unittest.main()
