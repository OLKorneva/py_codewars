# task: https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

from collections import Counter


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    d = Counter(walk)
    if d['n'] == d['s'] and d['w'] == d['e']:
        return True
    return False
