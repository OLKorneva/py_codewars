# task: https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python

def parse(data):
    num, res = 0, []
    for sym in data:
        if sym == 'i':
            num += 1
        elif sym == 'd':
            num -= 1
        elif sym == 's':
            num = num ** 2
        elif sym == 'o':
            res.append(num)
    return res