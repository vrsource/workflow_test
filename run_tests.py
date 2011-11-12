import random
import unittest

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.value = 10

    def test_case1(self):
        var = 5 + 5
        assert var == 10
        
    def test_test1(self):
        assert (1 == 1)
        

    def test_another(self):
        assert True        

if __name__ == '__main__':
    unittest.main()
