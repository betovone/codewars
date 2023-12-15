import unittest
from range_extraction_refactorizada import solution

class TestRangeExtraction(unittest.TestCase):
    def test_values(self):
        print("Test Range extraction")
        self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), "-6,-3-1,3-5,7-11,14,15,17-20")
        self.assertEqual(solution([-3,-2,-1,2,10,15,16,18,19,20]), "-3--1,2,10,15,16,18-20")
        self.assertEqual(solution( [-59, -58, -56, -55, -52, -50, -47, -44, -42, -39, -36, -35, -33, -31, -30, -29, -28, -25, -24, -23, -21, -19, -18, -16, -13, -10, -7, -5, -2, -1]), '-59,-58,-56,-55,-52,-50,-47,-44,-42,-39,-36,-35,-33,-31--28,-25--23,-21,-19,-18,-16,-13,-10,-7,-5,-2,-1')
        

