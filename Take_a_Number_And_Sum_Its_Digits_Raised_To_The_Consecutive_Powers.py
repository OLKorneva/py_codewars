# task: https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    # your code here
    res = []
    for i in range(a, b + 1):
        total = 0
        for ind, dig in enumerate(str(i), 1):
            total += int(dig) ** ind
        if total == i:
            res.append(i)

    return res