#task: https://www.codewars.com/kata/58065440a4647e0ed3000230/train/python


def find_max_range(ranges):
    res, total = [], None
    for r in ranges:
        lst = r.split()
        num1, num2 = float(lst[1]), float(lst[-1])
        if total is None or abs(num2 - num1) > total:
            total = abs(num2 - num1)
            res = [r]
        elif total == abs(num2 - num1):
            res.append(r)
    return res


print(find_max_range(["from 1 to 3","from 2 to 6","from -100 to 0"])) #["from -100 to 0"]

print(find_max_range(["from 1 to 3","from 2 to 4","from 1 to 1"])) #["from 1 to 3","from 2 to 4"]

print(find_max_range(["from 1 to 10","from 10 to 1","from -1 to -10"])) #["from 1 to 10","from 10 to 1","from -1 to -10"]

print(find_max_range(["from 1 to 10","from 10.1 to 1","from -1 to -10"])) #["from 10.1 to 1"]

print(find_max_range([])) #[]