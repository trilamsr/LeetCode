class Solution:
    def reverseParentheses(self, s: str) -> str:
        address = self.create_address(s)
        return ''.join(self.traverse(s, address))
        
    def traverse(self, s, address):
        i, direction = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = address[i]
                direction = -direction
            else:
                yield s[i]
            i += direction
        
    def create_address(self, s):
        stack, address = [], {}
        OPEN, CLOSED = '(', ')'
        for i, v in enumerate(s):
            if v == OPEN:
                stack.append(i)
            if v == CLOSED:
                head, tail = i, stack.pop()
                address[head], address[tail] = tail, head
        return address

class Solution:
    def reverseParentheses(self, s: str) -> str:
        OPEN, CLOSED = '(', ')'
        stack = []
        for char in s:
            if char != CLOSED: stack.append(char)
            else:
                substring = []
                while stack[-1] != OPEN:
                    substring.append(stack.pop())
                stack.pop()
                stack.extend(substring)
        return ''.join(stack)
