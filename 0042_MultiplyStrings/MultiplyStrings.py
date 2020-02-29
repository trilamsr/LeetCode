class Solution:
    def multiply_single_digit(self, num1, digit, start, ret):
        for num in num1:
            product = int(num)*int(digit)
            ret[start] = ret[start] + product
            start -= 1
    
    def mass_carry(self, arr):
        carry = 0
        for i in range(len(arr)-1, -1, -1):
            total = arr[i]+carry
            arr[i], carry = total%10, total//10
    
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        num1, num2 = num1[::-1], num2[::-1]
        ret = [0]*(len(num1)+len(num2))
        for i, digit in enumerate(num2):
            self.multiply_single_digit(num1, digit, len(ret)-1-i, ret)
        self.mass_carry(ret)
        return ''.join(str(ele) for ele in ret).lstrip('0')



class Solution:
    def __init__(self):        
        self.multiply_dict = {}
        self.sum_dict = {}
        for i in range(10):
            for j in range(10):
                self.multiply_dict[(str(i), str(j))] = i*j
                self.sum_dict[(str(i), str(j))] = i+j
                
    def digit_multiply(self, num1, digit, padding):
        carry = 0
        ret = collections.deque()
        for num in num1[::-1]:
            total = self.multiply_dict[num, digit] + carry
            cur_carry, remainder = total//10, total%10
            ret.appendleft(str(remainder))
            carry = cur_carry
        if carry: ret.appendleft(str(carry))
        for _ in range(padding):
            ret.append('0')
        return ''.join(ret)
    
    def total(self, a, b):
        if len(b) > len(a): return self.total(b, a)
        ret, carry = [], 0
        a, b = a[::-1], b[::-1]
        for i in range(len(a)):
            b_value = b[i] if i < len(b) else '0'
            total = self.sum_dict[a[i], b_value] + carry
            carry, remainder = divmod(total, 10)
            ret.append(str(remainder))
        if carry: ret.append(str(carry))
        while len(ret) > 1 and ret[len(ret)-1] == '0': ret.pop()
        return ''.join(ret[::-1])
    
    def multiply(self, num1: str, num2: str) -> str:
        ret = "0"
        for offset, digit in enumerate(num2):
            padding = len(num2)-1-offset
            cur_product = self.digit_multiply(num1, digit, padding)
            ret = self.total(ret, cur_product)
        return ret



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = 0
        for offset, digit in enumerate(num2):
            padding = len(num2)-1-offset
            cur_product = self.digit_multiply(int(num1), int(digit), padding)
            ret = sum([ret, cur_product])
        return str(ret)
    
    def digit_multiply(self, num1, digit, padding):
        ret = num1*digit
        for _ in range(padding):
            ret = ret*10
        return ret



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = self.parse_int(num1)
        b = self.parse_int(num2)
        return str(a*b)
    
    def parse_int(self,num):
        ret = 0
        for digit in num:
            ret = ret*10+int(digit)
        return ret

