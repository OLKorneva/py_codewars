# task: https://www.codewars.com/kata/541c8630095125aba6000c00/train/python


def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))