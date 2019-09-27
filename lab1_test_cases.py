import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """raises ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_2(self):
        """test for empty int_list"""
        int_list = []
        self.assertEqual(max_list_iter(int_list), None)        

    def test_max_list_iter_3(self):
        """test for max in list of length 5"""
        self.assertEqual(max_list_iter([4,67,76,2,19]),76)

    def test_reverse_rec(self):
        """reverses list of length 3"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_1(self):
        """test if list is None"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_reverse_rec_2(self):
        """list of length 1"""
        self.assertEqual(reverse_rec([1]),[1])

    def test_bin_search(self):
        """target = middle"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_1(self):
        """Raises ValueError"""
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 9, tlist)    

    def test_bin_search_2(self):
        """target not found"""
        int_list = [0,1,4,5,6,8,11]
        low = 0
        high = len(int_list)-1
        self.assertEqual(bin_search(7,low,high,int_list), None)

    def test_bin_search_3(self):
        """target > middle index"""
        int_list = [1,2,3,4,5,6,7]
        low = 0
        high = len(int_list)-1
        self.assertEqual(bin_search(6,low,high,int_list), 5)

    def test_bin_search_4(self):
        """Target < middle index"""
        int_list = [2,3,4,8,9,23]
        low = 0
        high = len(int_list)-1
        self.assertEqual(bin_search(3,low,high,int_list), 1)

if __name__ == "__main__":
        unittest.main()

    
