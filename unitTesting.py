import unittest
import selfMadeLibary

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(selfMadeLibary.Values.valuePlusOne(2), 3)

    def test_negative(self):
        self.assertEqual(selfMadeLibary.Values.valuePlusOne(-1), 0)

if __name__ == "__main__":
    unittest.main()