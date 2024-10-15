# task: https://www.codewars.com/kata/57cf50a7eca2603de0000090


def move_ten(st):
    res = []
    for s in st:
        num = ord(s) + 10
        letter = num if num <= 122 else num - 26
        res.append(chr(letter))
    return ''.join(res)


print(move_ten('testcase')) # "docdmkco"