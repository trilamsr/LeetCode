from collections import defaultdict

def build_frequency(s, mem):
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num_start = i
        while i < len(s) and str(s[i]).isnumeric():
            i += 1
        mem[char] += int(s[num_start:i])

def merge(a, b, key):
    ret = []
    a_i = b_i = 0
    while a_i < len(a) and b_i < len(b):
        if key(a[a_i]) < key(b[b_i]):
            ret.append(a[a_i])
            a_i += 1
        else:
            ret.append(b[b_i])
            b_i += 1
    ret.extend(a[a_i:] + b[b_i:])
    return ret

def merge_sort(arr, key):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def betterCompression(s):
    mem = defaultdict(int)
    build_frequency(s, mem)
    def sort_key(x): return x[0]
    ret = "".join([k+str(v) for k, v in merge_sort(list(mem.items()), sort_key)])
    return ret


