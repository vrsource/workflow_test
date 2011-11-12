import random
import unittest

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.value = 10
        
    def test_part2(self):
        assert 2 == 2

    def test_case1(self):
        var = 5 + 5
        assert var == 10
        
    def test_test1(self):
        assert (1 == 1)
        
    def test_another(self):
        assert True        

class TestOtherStuff(unittest.TestCase):
    def test1(self):
        assert 2 == 2        

    def test2(self):
        assert 3 == 3

    def test3(self):
        assert 4 == 4


if __name__ == '__main__':
    print "Starting test suite"
    unittest.main()
