# task: https://www.codewars.com/kata/5a9e86705ee396d6be000091


def check_three_and_two(array):
    a, b, c = 0, 0, 0
    for item in array:
        if item == 'a':
            a += 1
        elif item == 'b':
            b += 1
        elif item == 'c':
            c += 1
    return 3 in (a, b, c) and 2 in (a, b, c)

