# task: https://www.codewars.com/kata/59c633e7dcc4053512000073
import re

def solve(s):
    substrs = re.split(r'[aeiou]+', s.lower())
    largest = 0
    for substr in substrs:
        total = sum(map(lambda x: ord(x) - 96, substr))
        if total > largest:
            largest = total
    return largest


lst = ["zodiac", "strength"]
for s in lst:
    print(solve(s))

