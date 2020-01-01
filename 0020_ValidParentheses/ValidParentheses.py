class Solution:
    def isValid(self, s: str) -> bool:
        mem = { ']': '[', ')': '(', '}': '{' }
        stack = []
        for char in s:
            if char not in mem: stack.append(char)
            else:
                if not stack: return False
                if stack.pop() != mem[char]: return False
        return len(stack) == 0

