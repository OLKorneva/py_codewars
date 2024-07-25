# task: https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    a, b, c = integers[:3]
    if a % 2 == b % 2 or a % 2 == c % 2:
        balance = a % 2
    else:
        balance = b % 2
    for num in integers:
        if num % 2 != balance:
            return num


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))