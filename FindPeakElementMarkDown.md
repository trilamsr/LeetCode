### Intuition
```
actual representation:
This is actually a discrete polynomial function: 
  SUM(c_i * x^i) for i in [1..n]
  ex: 3x^3 + 2x^2 + x^1 + 2

    peak1
      V        peak2
      -         V
    -   -       -
  -      -     - -
-         -   -   -
            -      -
            ^        -
           valley


given a single peak:
    peak1
      V     
      -    
    -   -  
  -      -  
-         -   

this is a discrete polynomial that is negative parabola

            




peak element: binary search on a continuous derivative function

          
if sign of derivative is positive: then you are increasing
if sign of derivative is negative: then you are decreasing

problem is telling you to find the local maxima
-> if u remember ur calc: point where sign of derivative changes from (+) -> (-)
-> find lowerbound on decreasing sequence -> P(x): nums[x] > nums[x+1]


( if you look at the graph, there is ordering in the sense that its stricly decreasing )

: GRAPH OF DERIVATIVE



  \                           (+)
   \                /\
    \              /  \
     \            /    \
      \          /      \
------------- ------- -----------0
        \       / ^       ^\  (-)
      ^  \     /  valley p2 \
    p1    \   /              \
           \ / 



: GRAPH OF DERIVATIVE

  \                           (+)
   \                /\
    \              /  \
     \            /    \
      \          /      \
------------- ------- -----------0
        \       / ^       ^\  (-)
      ^  \     /  valley p2 \
    p1    \   /              \
           \ / 

[-----------]
    ^
(if we are on this interval,
then we never check other
mountain)


: GRAPH OF DERIVATIVE
  \                           (+)
   \                /\
    \              /  \
     \            /    \
      \          /      \
------------- ------- -----------0
        \       / ^       ^\  (-)
      ^  \     /  valley p2 \
    p1    \   /              \
           \ / 

            [---------------]
                  ^
          (likewise if we are on this interval,
          then we never check other
          mountain)


: GRAPH OF DERIVATIVE
  \                           (+)
   \                /\
    \              /  \
     \            /    \
      \          /      \
------------- ------- -----------0
        \       / ^       ^\  (-)
      ^  \     /  valley p2 \
    p1    \   /              \
           \ / 

            [---------------]
                  ^
          (likewise if we are on this interval,
          then we never check other
          mountain)

: IF THERE ARE MULTIPLE VALLEYS
: we will keep reducing the valleys and peaks
: so at the end this will reduce down to 
: finding the deriative if negative parabola
: d/dx(-x^2) = -x
              (this is negative slope)

  \          (+)
   \   
    \   
     \    
      \  
------------- 0
      ^ \
    peak \    (-)
          \    
           \ 
            \

  (a point where number increases, then decreases) 


```

### Implementation 
```python
def lower_bound(nums, property):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if property(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        is_decreasing = lambda x: x == len(nums) -1  or (nums[x+1] - nums[x] < 0)
        return lower_bound(nums, is_decreasing)
    
# property is_decreasing : means its last element or negative de
#  negative derivative: nums[x+1] - nums[x] < 0 or nums[x+1] < nums[x]
# last-element since nums[-1] = nums[n] = -∞.
```