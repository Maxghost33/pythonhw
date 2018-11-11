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
        print("\nTest for func 'return_str()'")
    def tearDown(self):
        print ("Finish tests for func 'return_str()'")


class Sum(unittest.TestCase):
    
    def test_sum_success(self):
        self.assertEqual(self.result, summ(self.args))
    
    def test_sum_str(self):
        with self.assertRaises(Exception):
            summ(self.arg_str)   

    @classmethod
    def setUpClass(cls):
        cls.args = [1, 2, 3, 4]
        cls.result = 10
        cls.arg_str = ['a', 'b', 'c']
    
    def setUp(self):
        print("\nTest for func 'Summ()'")
    def tearDown(self):
        print ("Finish tests for func 'Summ()'")


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
        print("\nTest for func 'Multiply()'")
    def tearDown(self):
        print ("Finish tests for func 'Multiply()'")

class reverse_test(unittest.TestCase):
    
    def test_reverse_success(self):
        self.assertEqual(self.result, reverse(self.args))
    
    def test_reverse_int(self):
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
        print("\nTest for func 'Reverse()'")
    def tearDown(self):
        print ("Finish tests for func 'Reverse()'")

class IsPalindrome_test(unittest.TestCase):
    
    def test_ispal_success(self):
        self.assertTrue(isPalindrome(self.args))
    
    def test_ispal_fail(self):
        self.assertFalse(isPalindrome(self.fail))
    
    def test_ispal_int(self):
        with self.assertRaises(Exception):
            isPalindrome(self.integer)
    
    def test_ispal_case(self):
        self.assertTrue(isPalindrome(self.case))
    
    @classmethod
    def setUpClass(cls):
        cls.args = "radar"
        cls.fail = "qradar"
        cls.case = "RadAr"
        cls.integer = 123456
    
    def setUp(self):
        print("\nTest for func 'isPalindrome()'")
    def tearDown(self):
        print ("Finish tests for func 'isPalindrome()'")


class histogram_test(unittest.TestCase):
    
    def test_hist_success(self):
        self.assertEqual(self.result, histogram(self.args))
    
    def test_hist_str(self):
        with self.assertRaises(Exception):
            histogram(self.arg_str)   

    @classmethod
    def setUpClass(cls):
        cls.args = [3, 0, 4]
        cls.result = ['***', '', '****']
        cls.arg_str = ["a", 3, -4]
    
    def setUp(self):
        print("\nTest for func 'Histogram()'")
    def tearDown(self):
        print ("Finish tests for func 'Histogram()'")

class caesarCipher_test(unittest.TestCase):
    
    def test_cipher_success(self):
        self.assertEqual(self.result, caesarCipher(self.args, self.key))
    
    def test_cipher_str(self):
        with self.assertRaises(Exception):
            caesarCipher(self.arg_str, self.key)   

    @classmethod
    def setUpClass(cls):
        cls.args = "abczyw"
        cls.empty = ""
        cls.key = 4
        cls.result = "efgdca"
        cls.resempty = ""
        cls.arg_str = "###@"
    
    def setUp(self):
        print("\nTest for func 'caesarCipher()'")
    def tearDown(self):
        print ("Finish tests for func 'caesarCipher()'")


class diagonalReverse_test(unittest.TestCase):
    
    def test_diagrev_success(self):
        self.assertEqual(self.result, diagonalReverse(self.args))
    
    def test_diagrev_successstr(self):
        self.assertEqual(self.result_str, diagonalReverse(self.args_str))
    
    def test_diagrev_successstr(self):
        self.assertEqual(self.result_mix, diagonalReverse(self.args_mix))
    
    def test_diagrev_str(self):
        with self.assertRaises(Exception):
            diagonalReverse(self.arg_str)
    
    def test_diagrev_success_no_same(self):
        self.assertEqual(self.result, diagonalReverse(self.args_same))

    @classmethod
    def setUpClass(cls):
        cls.args = [[1,2,3], [4,5,6], [7,8,9]]
        cls.result = [[1,4,7], [2,5,8], [3,6,9]]
        cls.args_str = [['a','b','c'], ['d','e','j'], ['h','k','l']]
        cls.result_str = [['a','d','h'], ['b','e','k'], ['c','j','l']]
        cls.args_mix = [['a','',''], ['2','',''], ['#','','']]
        cls.result_mix = [['a','2','#'], ['','',''], ['','','']]
        cls.arg_str = "qwe3"
        cls.args_same = [[1,2,3], [4,5,6,'',4,10], [7,8,9,9]]
    
    def setUp(self):
        print("\nTest for func 'diagonalReverse()'")
    def tearDown(self):
        print ("Finish tests for func 'diagonalReverse()'")


class game_test(unittest.TestCase):
    
    def test_game_success(self):
        self.assertTrue(game(self.a, self.b))

    @classmethod
    def setUpClass(cls):
        cls.a = 1
        cls.b = 10
    
    def setUp(self):
        print("\nTest for func 'Game()'")
    def tearDown(self):
        print ("Finish tests for func 'Game()'")

class balanced_test(unittest.TestCase):
    
    def test_balanced_success(self):
        self.assertTrue(balanced_str(self.a))
    
    def test_balanced_fail(self):
        self.assertFalse(balanced_str(self.b))

    @classmethod
    def setUpClass(cls):
        cls.a = "[[][[]]]"
        cls.b = "][[[]]"
    
    def setUp(self):
        print("\nTest for func 'Balanced_str()'")
    def tearDown(self):
        print ("Finish tests for func 'Balanced_str()'")

class charFreq_test(unittest.TestCase):
    
    def test_charF_success(self):
        self.assertEqual(self.result, charFreq(self.a))
    
    def test_charF_empty(self):
        self.assertEqual(self.res, charFreq(self.b))

    @classmethod
    def setUpClass(cls):
        cls.a = "aabbaeeba"
        cls.result = {"a": 4, "b": 3, "e": 2}
        cls.b = ""
        cls.res = {}
    
    def setUp(self):
        print("\nTest for func 'charFreq()'")
    def tearDown(self):
        print ("Finish tests for func 'charFreq()'")

class dec_to_bin_test(unittest.TestCase):
    
    def test_dec_to_bin_success(self):
        self.assertEqual(self.result, decToBin(self.a))
    
    def test_dec_to_bin_empty(self):
        self.assertEqual(self.res, decToBin(self.b))
    
    def test_dec_to_bin_noint(self):
        with self.assertRaises(Exception):
            decToBin(self.c)

    @classmethod
    def setUpClass(cls):
        cls.a = 100
        cls.result = 1100100
        cls.b = 0
        cls.res = 0
        cls.c = -100
    
    def setUp(self):
        print("\nTest for func 'decToBin()'")
    def tearDown(self):
        print ("Finish tests for func 'decToBin()'")



if __name__=='__main__':
    unittest.main()



