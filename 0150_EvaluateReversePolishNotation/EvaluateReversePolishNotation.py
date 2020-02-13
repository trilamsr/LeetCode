class Solution:
    def division(self, x,y):
        is_positive = x > 0 and y > 0 or x < 0 and y < 0
        ret = abs(y)//abs(x)
        return ret if is_positive else -ret
        
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: y-x,
            '/': self.division,
            '*': lambda x,y: x*y
        }
        stack = []        
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                val = op[token](stack.pop(), stack.pop())
                stack.append(val)
        return stack[0]