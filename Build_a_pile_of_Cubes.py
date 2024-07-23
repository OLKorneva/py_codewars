#task: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

def find_nb(m):
    total = 1
    num = 1
    while total < m:
        num += 1
        total += num ** 3
    return num if total == m else -1


print(find_nb(1071225))
print(find_nb(91716553919377))