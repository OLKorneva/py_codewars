#task: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    return [el for el in a if el not in b]

print(array_diff([1,2,2,2,3],[2]))