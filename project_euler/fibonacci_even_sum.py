"""
From Project Euler:
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find
the sum of the even-valued terms.

I wrote a general solution
"""


def fibonacci_even_sum(num):
    """
    INPUT: an integer greater than or equal to zero
    OUTPUT: the sum of all even Fibonacci numbers less than the ith Fibonacci number,
            where i is equal to the input
    """
    even_lst = []
    if num == 0:
        return 0
    if num == 1:
        return 1
    first_num = 1
    second_num = 1
    while second_num <= num:
        temp_num = second_num
        second_num = first_num + second_num
        first_num = temp_num
        if second_num % 2 == 0:
           even_lst.append(second_num)
    return sum(even_lst)
