import unittest
from run import minus

class TestMinus(unittest.TestCase):
    def test_minus_function(self):
        self.assertEqual(minus(3, 1), 2)  
        self.assertEqual(minus(7, 4), 3)  

    def test_minus_function_with_floats(self):
        self.assertAlmostEqual(minus(5.2, 2.1), 3.1) 

if __name__ == "__main__":
    unittest.main()
