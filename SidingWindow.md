'''
general-idea: you have some input
and some properties that must hold
​
function f(input):
    
    so you got your window
    window = ...
​
    for each element in input:
​
        1. add the element to window
        
        2. make your window into a valid window
            - while the window is not valid:
                - update the window
​
        3. so you have a valid window
            - do something with this window
​
​
so question is:
- how can we do #2 efficiently as possible
​
'''


class SlidingWindow:
​
    def __init__(self, ...):
        pass
​
    def __len__(self):
        pass
​
    def append(self, ...):
        pass
​
    def pop_left(self, ...):
        pass
​
    def satisfies_property(self, ...):
        pass
​
​
def problem(some_input):
​
    window = SlidingWindow(...)
    ret = some value that you want to compare to window
​
    for element in some_input:
        window.append(element)
​
        while not window.satisfies_property(element):
            window.popleft(...)
​
        # now you have a valid window
        ret = max(ret, len(window))
​
    return ret




-----------------------------------------
from collections import defaultdict
​
class SlidingWindow:
    
    def __init__(self):
        self.window = defaultdict(int)
        self.lo = 0
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def append(self, ch):
        self.window[ch] += 1
        self.size += 1
    
    def pop_left(self, string):
        self.window[string[self.lo]] -= 1
        self.lo += 1
        self.size -= 1
    
    def satisfies_property(self, ch):
        return self.window[ch] <= 1
​
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        window = SlidingWindow()
        ret = 0
        
        for ch in s:
            window.append(ch)
            
            while not window.satisfies_property(ch):
                window.pop_left(s)
​
            ret = max(ret, len(window))
            
        return ret




---------------------------------------
from collections import Counter
from string import ascii_lowercase
​
class SlidingWindow:
    
    # O(pattern)
    def __init__(self, pattern):
        self.table = Counter()
        self.target = Counter(pattern)
        self.lo = 0
        self.size = 0
        self.constraint = len(pattern)
        
    def append(self, ch):
        self.table[ch] += 1
        self.size += 1
    
    def pop_left(self, text):
        self.table[text[self.lo]] -= 1
        self.lo += 1
        self.size -= 1
    
    def satisfy_property(self):
        return self.size <= self.constraint
    
    def has_permutation(self):
        return all(self.table[ch] == self.target[ch] for ch in ascii_lowercase)
        
# time: O(pattern + 26*text) => O(pattern + text)
# space: O(26) for characters in alphabet -> O(1)
class Solution:
    def checkInclusion(self, pattern: str, text: str) -> bool:
        if len(pattern) > len(text): return False 
        
        window = SlidingWindow(pattern)
​
        for ch in text:
            window.append(ch)
            
            while not window.satisfy_property():
                window.pop_left(text)
            
            if window.has_permutation():
                return True
            
        return False
        
​
##############################################################################################################
​
from collections import Counter
from string import ascii_lowercase
from operator import mul
from functools import reduce
​
class SlidingWindow:
    
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    TABLE = dict(zip(ascii_lowercase, PRIMES))
    
    def __init__(self, pattern):
        self.target = reduce(mul,(SlidingWindow.TABLE[ch] for ch in pattern), 1)
        self.signature = 1
        self.lo = 0
        self.size = 0
        self.constraint = len(pattern)
        
    def __len__(self):
        return self.size
    
    def append(self, ch):
        self.signature *= SlidingWindow.TABLE[ch]
        self.size += 1
    
    def pop_left(self, text):
        ch = text[self.lo]
        self.signature //= SlidingWindow.TABLE[ch]
        self.lo += 1
        self.size -= 1
    
    def satisfies_property(self):
        return self.size <= self.constraint
    
    def has_permutation(self):
        return self.signature == self.target
​
class Solution:
    def checkInclusion(self, pattern: str, text: str) -> bool:
        if len(pattern) > len(text): return False 
​
        window = SlidingWindow(pattern)
​
        for ch in text:
            window.append(ch)
            
            while not window.satisfies_property():
                window.pop_left(text)
            
            if window.has_permutation():
                return True
            
        return False