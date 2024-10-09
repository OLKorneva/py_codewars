# task: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    return [num for num in lst if num != 0] + [0] * lst.count(0)

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]