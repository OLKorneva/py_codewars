#task: https://www.codewars.com/kata/67191920c29c7e09d9f40707/train/python
from operator import add, sub


def digit_multiplication(expression):
    total = 0
    num = 1
    sign = add
    for item in expression:
        if item not in '+-':
            num *= int(item)
        else:
            total = sign(total, num)
            num = 1
            if item == '+':
                sign = add
            else:
                sign = sub
    return sign(total, num)


print(digit_multiplication("53+5"))
print(digit_multiplication("266-66"))
print(digit_multiplication("555"))
print(digit_multiplication("3434343-12121212+4949494-122"))