class Solution:
    def compress(self, chars: List[str]) -> int:
        left = i = 0
        while i < len(chars):
            chars[left], count = chars[i], 1
            while i + 1 < len(chars) and chars[left] == chars[i+1]:
                count, i  = count + 1, i + 1
            if count > 1:
                for digit in self.compress_count(count):
                    left += 1
                    chars[left] = digit
            left, i = left + 1, i + 1
        return left
    
    def compress_count(self, count):
        for digit in str(count):
            yield digit
            