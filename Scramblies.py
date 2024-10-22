# task: https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
from collections import Counter


def scramble(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    for letter, num in c2.items():
        if c1.get(letter, 0) < num:
            return False
    return True


print(scramble('rkqodlw', 'world')) # True
print(scramble('cedewaraaossoqqyt', 'codewars')) # True
print(scramble('katas', 'steak')) # False

