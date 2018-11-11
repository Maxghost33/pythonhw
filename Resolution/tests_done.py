import unittest
from tasks_done import *

class Return_Str_Test(unittest.TestCase):
    
    def test_print_success(self):
        self.assertEqual(self.s, return_str(self.arg))

    @classmethod
    def setUpClass(cls):
        cls.arg = input("Set value for test: ")
        cls.s = '"Hello, ' + cls.arg + '!"'
    def setUp(self):
        print("Test for func 'return_str()'")
    def tearDown(self):
        print ("Finish tests for func 'return_str()'")


class Sum(unittest.TestCase):
    
    def test_sum_success(self):
        self.assertEqual(self.result, sum(self.args))
    
    def test_sum_str(self):
        with self.assertRaises(Exception):
            sum(self.arg_str)   

    @classmethod
    def setUpClass(cls):
        cls.args = [1, 2, 3, 4]
        cls.result = 10
        cls.arg_str = ['a', 'b', 'c']
    
    def setUp(self):
        print("Test for func 'Sum()'")
    def tearDown(self):
        print ("Finish tests for func 'Sum()'")


class Multiply_test(unittest.TestCase):
    
    def test_mult_success(self):
        self.assertEqual(self.result, multiply(self.args))
    
    def test_mult_str(self):
        with self.assertRaises(Exception):
            multiply(self.arg_str)   

    @classmethod
    def setUpClass(cls):
        cls.args = [1, 2, 3, 4]
        cls.result = 24
        cls.arg_str = ['a', 'b', 'c']
    
    def setUp(self):
        print("Test for func 'Multiply()'")
    def tearDown(self):
        print ("Finish tests for func 'Multiply()'")

class reverse_test(unittest.TestCase):
    
    def test_reverse_success(self):
        self.assertEqual(self.result, reverse(self.args))
    
    def test_mult_int(self):
        with self.assertRaises(Exception):
            reverse(self.integer)
    def test_reverse_case(self):
        count = len(self.args) - 1
        for i in self.args:
            self.assertTrue(i == reverse(self.args)[count])
            count -= 1
    @classmethod
    def setUpClass(cls):
        cls.args = "I am testing"
        cls.result = "gnitset ma I"
        cls.integer = 123456
    
    def setUp(self):
        print("Test for func 'Reverse()'")
    def tearDown(self):
        print ("Finish tests for func 'Reverse()'")

if __name__=='__main__':
    unittest.main()



