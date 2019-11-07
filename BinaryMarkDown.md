

### standard binary search algorithm
```
| you have a window [lo..hi]
| you want to look for some target

  target
    V
[.......|.......]
^       ^       ^
lo      mid     hi

-> since target is in between [lo..mid]:
search between [lo..mid]
```
### algorithm
```python
def find(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### insight
```
  target
    V
[.......|.......]
^       ^       ^
lo      mid     hi

this means that every item >= mid:
    | is also greater than target
    | this insight tells us that we can search
      on properties of the problem

```

### example of searching on non-sorted values
```
given a list that is [ ... even #s ... | odd #s ...]
find the first index where it's odd
example:
[2,4,6,10,-2,-8,20,1,3,5,7]
                   ^
                this should be the answer

this question is equivalent to find the first index
in the list that satisfies the 'odd' property
[2,4,6,10,-2,-8,20,1,3,5,7]
 F F F  F  F  F  F T T T T

- notice that this list is not even 'sorted'
but it's sorted in the sense that you can translate
F -> 0
T -> 1

[2,4,6,10,-2,-8,20,1,3,5,7]
F F F F F F F T T T T
0 0 0 0 0 0 0 1 1 1 1

-> this question is equivalent to find the lower-bound of oddness
-> on the flip side, if we find the upper-bound of evenness:
    we can find the next odd by adding + 1

[2,4,6,10,-2,-8,20,1,3,5,7]
TTTTTTTFFFFF
      ^
      (last index of true)
      (so first index of false is the first odd number)

```

### implementation
```python
# lower-bound of oddness
def find_first_odd(nums):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if odd(nums[mid]):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

# upper-bound of evenness
def find_first_odd(nums):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if even(nums[mid]):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi + 1 (<- add +1 since this gives us last index of even number)

```

### insight
```python
now, we got 3 binary search algorithms
- standard
- lower-bound
- upper-bound

# standard
def find(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# given some property p
def lower_bound(nums):
    lo, hi = 0, len(nums) -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if P(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

def upper_bound(nums):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if P(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

# realisitcally upper_bound is just symmetric case of lower_bound

```


### QuestionList
```

https://leetcode.com/problems/first-bad-version/
https://leetcode.com/problems/sqrtx/
https://leetcode.com/problems/binary-search/
https://leetcode.com/problems/find-peak-element/
https://leetcode.com/problems/guess-number-higher-or-lower/
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
https://leetcode.com/problems/search-insert-position/
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
https://leetcode.com/problems/find-peak-element/
https://leetcode.com/problems/search-in-rotated-sorted-array/
https://leetcode.com/problems/median-of-two-sorted-arrays/

https://leetcode.com/problems/find-in-mountain-array/


```

def lower_bound(lo, hi, property):
    while lo <= hi:
        mid = (lo + hi) // 2
        if property(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo
​
def upper_bound(lo, hi, property):
    while lo <= hi:
        mid = (lo + hi) // 2
        if property(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi
​
class Solution:
    def mySqrt(self, target):
        # lower-bound
        # P(x): x*x > target
        # find the smallest value where x&x>target
        # given 8
        # 2,3,4,5,
        # | | | |
        # 4 9 16 25
        # F T T T
        # but 9 > 8 and sqrt(8) is 2.814... and we want 2
        # so to negatate x*x > target -> x*x <= target
        #                                     ^ 
        #                                   this is the negation
        # just subtract 1
        
        #gt = lambda x: x*x > target
        #return lower_bound(1, target, gt)
        
        # upper-bound
        # P(x): x*x <= target
        # we want to find the greatest value where n * n <= target
        # given 8
        # 2,3,4
        # ^ ^ ^
        # 4 9 16
        #  -> 4 < 8 but 9 > 8 so return [2]
        lte = lambda x: x * x <= target
        return upper_bound(1, target, lte)

'''
Intuition:


       / 
      / 
     /
    /
   /
  /
 /
/
------------ <- end of array
            /
           /
          /
         /
        /
       /
       ^ 
      min_index

Assume:
  | the array is sorted
  | rotated k amount 

- it must mean that the last element has to be the
greatest element out of the last 'k' elements
- last element < first element

- visually this is obvious and so we can define 
Property P(x) : nums[x] <= (last element)

'''
def lower_bound(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return nums[lower_bound(nums, nums[-1])]