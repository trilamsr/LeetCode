class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret = (ret << 1) + ((n>>i)& 1)
        return ret

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret = (ret << 1) + (n & 1)
            n >>= 1
        return ret

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret = ret << 1
            ret = ret | (n & 1)
            n = n >> 1
        return ret

class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for i in range(32):
            bits.append(n & 1)
            n = n>>1
        ret = 0
        for bit in bits:
            ret = ret << 1
            ret |= bit
        return ret




# M_BRAX's

class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_mask = get_reverse_mask(n)
        return n ^ reverse_mask
    
def get_reverse_mask(n):
    ret = 0
    lo, hi = 0, 31
    while lo < hi:
        lo_bit = get_kth_bit(n, lo)
        hi_bit = get_kth_bit(n, hi)
        if lo_bit != hi_bit:
            ret |= (1 << lo) | (1 << hi)
        print((lo, hi), (bin(ret)[2:].rjust(32, '0')))
        lo += 1
        hi -= 1
    return ret

def get_kth_bit(n, k): return (n >> k) & 1


class Solution:
    def reverseBits(self, n: int) -> int:
        lo, hi = 0, 31
        while lo < hi:
            lo_bit = get_kth_bit(n, lo)
            hi_bit = get_kth_bit(n, hi)
            if lo_bit != hi_bit:
                n ^= (1 << lo)
                n ^= (1 << hi)
                # n ^= (1 << lo) | (1 << hi)
            lo += 1
            hi -= 1
        return ret
    
def get_bit(n, k): return (n >> k) & 1