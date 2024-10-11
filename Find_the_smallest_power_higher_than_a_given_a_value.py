# task: https://www.codewars.com/kata/56ba65c6a15703ac7e002075/train/python
from math import ceil


def find_next_power(val, pow_):
    return ceil(val**(1/pow_)) ** pow_



print(find_next_power(12385, 3)) # 13824
print(find_next_power(1245678, 5)) # 1419857