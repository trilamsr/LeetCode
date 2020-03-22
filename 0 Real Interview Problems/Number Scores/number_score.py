def count_seven(num):
    ret = 0
    while num:
        if num%10 == 7: ret += 1
        num = num//10
    return ret

def compute_number_score(num):
    score = 0
    score += count_seven(num)
    check_sequence_of_five = check_sequence_of_five(num)
    check_sequence_one_less = check_sequence_one_less(num)
    count_even_digit = count_even_digit(num)
    is_multiple_of_three = is_multiple_of_three(num)


