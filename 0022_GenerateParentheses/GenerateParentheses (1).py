class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        self.dfs(le = 0, ri = 0, state='', n=n, ret=ret)
        return ret
        
    def dfs(self, le, ri, state, n, ret):
        if le == n and ri == n: ret.append(state)
        if le < n: self.dfs(le+1, ri, state+'(', n, ret)
        if le > ri: self.dfs(le, ri+1, state+')', n, ret)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        queue = [('', 0, 0)]
        while queue:
            state, le, ri = queue.pop()
            if le == ri == n: ret.append(state)
            if le < n: queue.append((state+'(', le+1, ri))
            if le > ri: queue.append((state+')', le, ri+1))
        return ret

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack(0,0, [], [], n)
    
    def backtrack(self, le, ri, stack, ret, n):
        if le == n and ri == n:
            ret.append("".join(stack))
        if le < n:
            stack.append('(')
            self.backtrack(le+1, ri, stack, ret, n)
            stack.pop()
        if ri < le:
            stack.append(')')
            self.backtrack(le, ri+1, stack, ret, n)
            stack.pop()
        return ret
