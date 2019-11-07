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


Design a function that returns # of elements in an array. this array is sorted

Empty Case:
f([], 8) -> 0
f([], 0) -> 0
Nothing found:
f([1,1,1,2,2,2,5], 8) -> 0
Found:
f([1,1,1,1,1], 1) -> 5
Out of bound:
	f([1,2,3,4,5], 1000) -> 0
	f([1,2,3,4,5], -1)   -> 0
One element:
	f([1], 1) -> 1
	f([1], 0) -> 0

def lower_bound (lo, hi, prop):
	while lo <= hi:
		mid = (lo+hi)//2
		if prop(mid):
			hi = mid-1
else: 
lo = mid+1
return lo

def NumElement(arr, target):
	if not arr: return 0
	lower = lower_bound(0, len(arr)-1, lambda x: arr[x] >= target))
	upper = lower_bound(0, len(arr)-1, lambda x: arr[x] > target)-1
	if lower >= len(arr) or upper < 0: return 0
	return upper-lower+1



















Design a function that returns # of elements in an array. this array is sorted

# so high level algorithmic description

we will use the binary search to find the 1st index
use another binary search to find the 2nd index

if the first index <= 2nd index: this means that its valid
- case: first index = 2nd index: -> 1 element
- case first index < 2nd index: -> more than 1 element

will the data have any corrupted input i.e. None in between the array
… 90% of the time => NO (we addressed this part)


############################################################
test cases

Empty:
[], _ -> 0

out of bounds ->
left-hand-side  [1,2,3,4,5], -1 -> 0
right-hand-side [1,2,3,4,5], 1000 -> 0

no elements existing ->
[1,2,3,4,6], 5 -> 0

elements existing ->
single element: [1,2,3,4,5], 1 -> 1
                [1,2,3,4,5], 5 -> 1
 somewhere in between [1,2,3,4,5], 3 -> 1

k elements-existing
[1,2,3,5,6,7,8], 4 -> 6



implementation

# for now lets assume that we have a binary search that exists

# now lets implement binary search

def lower_bound(array, lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

def num_elements(array, target):
    if not array: return 0
    lo = lower_bound(array, 0, len(array) - 1, target)
    hi = lower_bound(array, lo, len(array) - 1, target + 1) - 1
    return (hi - lo + 1) if lo <= hi else 0


##### DONE

