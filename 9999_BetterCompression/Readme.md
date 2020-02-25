# 9999 Better Compression


Consider a string, S, that is a series of characters, each followed by its frequency as an integer. The string is not compressed correctly, so there may be many occurences of the same character. A properly compressed string will consist of one intance of each character in alphabetical order, follwed by the total count of that character within the string.

 
**Constrains:**

   1. 1 <= size of S <= 100000
   2. 'a' <= characters in S <= 'z'
   3. 1 <= frequency of each racter in S <= 1000

**Example 1:**

    Input: 
        "a3c9b2c1"
    Output:
        "a3b2c10"
    Explanation:
        The string 'a3c9b2c1' has two instances where 'c' is followed by a count: once with 9 occurance, and again with 1. It should be compressed to 'a3b2c10'