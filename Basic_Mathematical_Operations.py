# task https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python

def basic_op(operator, value1, value2):
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return d[operator](value1, value2)

print(basic_op('/', 70, 7))