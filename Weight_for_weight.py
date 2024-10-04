# task: https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python


def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda x: (sum(map(int, x)), x)))


print(order_weight("56 65 74 100 99 68 86 180 90"))