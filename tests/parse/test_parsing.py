import unittest

from elena.parse.parser import *


class TestParsing(unittest.TestCase):
    def test_parseCheck(self):
        nodeStorage = parse("/Users/avaneesh/amherst")
        self.assertEqual(len(nodeStorage.nodeMap), 45071)


if __name__ == '__main__':
    unittest.main()
