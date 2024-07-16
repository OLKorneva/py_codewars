# task: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    count = 0
    while len(str(n)) > 1:
        count += 1
        digs = map(int, str(n))
        n = 1
        for dig in digs:
            n *= dig
    return count


print(persistence(4))
