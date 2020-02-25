import unittest

class IntersectionTest(unittest.TestCase):

    def test_empty(self):
        self.assertEquals(intersection([], []), [])
        self.assertEquals(intersection([], [1,2,3]), [])
        self.assertEquals(intersection([1,2,3], []), [])

    def test_no_intersection(self):
        self.assertEquals(intersection([1,2,3,4,5], [6,7,8,9,10]), [])
        self.assertEquals(intersection([1,2,3], [4,5,6]), [])

    def test_different_sizes(self):
        self.assertEquals(intersection([1,2,3,4,5], [6,7,8]), [])
        self.assertEquals(intersection([1,2,3,4,5], [4]), [4])
        self.assertEquals(intersection([1,2,3,4,5], [-1,0,3,5]), [3,5])

    def test_all_intersections(self):
        self.assertEquals(intersection([1,2,3,4,5], [1,2,3,4,5]), [1,2,3,4,5])
        self.assertEquals(intersection([1,2,3,4,5], [1,2,3]), [1,2,3])
        self.assertEquals(intersection([1,2,3], [1,2,3,4,5]), [1,2,3])

    def test_duplicate_cases(self):
        self.assertEquals(intersection([1,2,3,4,5], [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5]), [1,2,3,4,5])
        self.assertEquals(intersection([1,1,1,1,1,1,1,1,1,1,2,3,4,5], [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5]), [1,2,3,4,5])


def intersection(A, B):
    if not A or not B: 
        return []
    ret = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            val = A[i]
            ret.append(A[i])
            while i < len(A) and A[i] == val:
                i += 1
            while j < len(B) and B[j] == val:
                j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return ret

if __name__ == '__main__':
    unittest.main()