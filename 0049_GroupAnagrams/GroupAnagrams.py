class Solution:
    class Solution:
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        self.ret = collections.defaultdict(list)
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list(map(self.add_class, strs))
        return self.ret.values() 
        
    def add_class(self, string):
        classes = 1
        for char in string:
            classes *= self.primes[ord(char)%97]
        self.ret[classes].append(string)
            

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = collections.defaultdict(list)
        for cur in strs:
            ret["".join(sorted(cur))].append(cur)
        return ret.values()