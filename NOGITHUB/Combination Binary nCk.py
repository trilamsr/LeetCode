
def iter_combinations(k, upper_bound):
    bitset = (1 << (upper_bound-k)) - 1
    N = (1 << upper_bound)
    while bitset < N:
        yield bitset
        bitset = next_combination(bitset)
        
def next_combination(val):
    x = val & -val
    y = val + x
    z = ((val & ~y) // x) >> 1
    return y | z

def rev(n, k):
    ret = 0
    while k:
        ret <<= 1
        ret += (n & 1)
        n >>= 1
        k -= 1
    return ret

N=10
it = iter_combinations(k=3, upper_bound=N)
for val in it:
    word = bin(rev(~val, N))[2:].rjust(N, '.').replace('0', '.').replace('1','X')[::-1]
    print(word)

