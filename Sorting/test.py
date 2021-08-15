import random
from Sorting.bubble_sort import bubble
from Sorting.insertion_sort import insertion_sort_ascedning
from Sorting.quicksort import quick_sort
from Sorting.selection import selection_srot
from unittest import TestCase
import time

class  TestSum(TestCase):
    def test_quick(self):
        test_lst=[2,3,4,5,1,7,8,9,10,0,6]
        start=time.perf_counter()
        result = quick_sort(test_lst)
        end=time.perf_counter()
        print("Quick:","{:e}".format(end-start))
        self.assertEqual(result, [0,1,2,3,4,5,6,7,8,9,10])

    def test_bubble(self):
        test_lst = [2, 3, 4, 5, 1, 7, 8, 9, 10, 0, 6]
        start = time.perf_counter()
        result = bubble(test_lst)
        end = time.perf_counter()
        print("Bubble:", "{:e}".format(end - start))
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


    def test_insertion(self):
        test_lst = [2, 3, 4, 5, 1, 7, 8, 9, 10, 0, 6]
        start = time.perf_counter()
        result = insertion_sort_ascedning(test_lst)
        end = time.perf_counter()
        print("Insertion:", "{:e}".format(end - start))
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_selection(self):
        test_lst = [2, 3, 4, 5, 1, 7, 8, 9, 10, 0, 6]
        start = time.perf_counter()
        result = selection_srot(test_lst)
        end = time.perf_counter()
        print("Selection:", "{:e}".format(end - start))
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



if __name__ == '__main__':
    import unittest
    unittest.main()