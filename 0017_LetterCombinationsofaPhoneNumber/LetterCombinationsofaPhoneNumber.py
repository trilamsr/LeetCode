class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '1': "",
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        ret, stack = [], []
        if not digits: return ret
        self.dfs(mapping, ret, stack, digits, 0)
        return ret
    
    def dfs(self, mapping, ret, stack, digits, ind):
        if ind > len(digits): return
        if len(stack) == len(digits):
            ret.append(''.join(stack))
            return
        for char in mapping[digits[ind]]:
            stack.append(char)
            self.dfs(mapping, ret, stack, digits, ind+1) 
            stack.pop()