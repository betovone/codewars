import unittest
from sum_of_intervals import sum_of_intervals

class TestSumOfIntervals(unittest.TestCase):
    def test_values(self):
        print("test sum of intervals")
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]),  8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]),  4)
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]),  7)
        self.assertEqual(sum_of_intervals([(-1000000000, 1000000000)]),  2000000000)
        self.assertEqual(sum_of_intervals([(0, 20), (-100000000, 10), (30, 40)]),  100000030)
        self.assertEqual(sum_of_intervals([(10, 462), (45, 402), (107, 456), (270, 453), (234, 268), (224, 264)]) ,  452)
        self.assertRaises(ValueError, sum_of_intervals, "aaaa")
        self.assertRaises(ValueError, sum_of_intervals, ["aaaa"])
        self.assertRaises(ValueError, sum_of_intervals, [])
        self.assertRaises(ValueError, sum_of_intervals, [(10.1)])
        self.assertRaises(TypeError, sum_of_intervals, [(10,2), (3, "aaaa")])
        
        

