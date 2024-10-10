# task: https://www.codewars.com/kata/546e2562b03326a88e000020


def square_digits(num):
    return int(''.join([str(int(n)**2) for n in str(num)]))


print(square_digits(9119))