# 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

**Example:**

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1








'''

            ROOT = LCA = EMPTY
             -----------------

     1             2        3        4
     |             |        |        | 
------------    -------   ------   -------
2    3      4    1  3  4  1  2  4  1  2  3  
|    |      |    |  |  |  |  |  |  |  |  |  
3  2 - 4  2 - 3  3  1  1  2  1  1  2  1  1
|  |   |  |   |  |  |  |  |  |  |  |  |  |
4  4   2  3   2  4  4  3  4  4  2  3  3  2



ex: if we want to go from 1432 -> 2134
-> we need to crawl from 
    - 1->3->4-> [LCA_CHILD=1] -> [LCA=ROOT] -> [LCA_CHILD=2] -> 1 -> 3 -> 4
    - hit the LCA (ROOT=EMPTY)
    - crawl down: 2->1->3->4

okay u get this,
look what happens to the values while we're crawling up to the LCA

this means in the for loop:
for i in range(4):
    i = 0 IS DONE

which means its time to climb back up
2 -> 3 -> 4 -> 1

now its:
for i in range(4):
    'i is now 1'

we want the NEXT GREATEST VALUE
since 4-3->2 is the maximum possible value we can get... for this branch
            1                                       1
            | -> REVERSE (EVERYTHING BELOW 1) ->    |
            ..........................................
            4                                       2
            |                                       |
            3                                       3
            |                                       |
            2                                       4

-> we flip everything below SUBROOT
to MINIMIZE it!
4->3->2 -> [2->3->4]


currently subroot = 1 and now WE WANT TO TRANSITION INTO
subroot = 2

 
    here          here
     1   --------> 2        3        4
     |             |        |        | 
------------    -------   ------   -------
2    3      4    1  3  4  1  2  4  1  2  3  
|    |      |    |  |  |  |  |  |  |  |  |  
3  2 - 4  2 - 3  3  1  1  2  1  1  2  1  1
|  |   |  |   |  |  |  |  |  |  |  |  |  |
4  4   2  3   2  4  4  3  4  4  2  3  3  2


so temporarily we have....
1 | [2,3,4]
since we reversed 1|[4,3,2] -> 1|[2,3,4]

to PUT 1 into the CORRECT PLACE:
use binary search on [2,3,4]

[DONE]
'''
