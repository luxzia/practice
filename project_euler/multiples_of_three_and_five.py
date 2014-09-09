"""
This is a solution for Project Euler: 
Find the sum of all the multiples of 3 or 5 below 1000
"""

multiple_list = [x for x in xrange(1000) if x % 5 == 0 or x % 3 == 0]
multiples_sum = sum(multiple_list)

