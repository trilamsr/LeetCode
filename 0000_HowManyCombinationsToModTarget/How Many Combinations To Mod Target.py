# Given n, which is a length of the string, and mod_target m. How combination of the valid string's value is divisible m with no residual.

# Valid string is of length n
# Valid string contains character a-z
# Valid string is a string whose characters is sorted in ascending order
    # I.E.: abc, aaa, abcddde
    # Invalid string samples are: adc, abdc

# A value of string is the summation of the values of its characters.
# A value of a character is 0-26 corresponding to a-z

def combination_generator(str_len, start_point, stack):
    if len(stack) == str_len:
        yield ''.join(stack), get_val(stack)
        return
    for ascii_value in range(ord(start_point), ord('z')+1):
        stack.append(chr(ascii_value))
        yield from combination_generator(str_len, chr(ascii_value), stack)
        stack.pop()

def get_val(stack):
    return sum([ord(c)-97 for c in stack])

def num_combination(str_len, mod_target):
    ret = 0
    for str, val in combination_generator(str_len, 'a', []):
        print(str, val)
        if val % mod_target == 0: ret += 1
    return ret

actual = num_combination(2, 10)
print(actual)