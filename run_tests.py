import random
import unittest

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.value = 10

    def test_case1(self):
        var = 5 + 5
        assert var == 10
        

if __name__ == '__main__':
    unittest.main()
