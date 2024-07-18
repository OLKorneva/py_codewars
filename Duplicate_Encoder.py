# task: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
from collections import Counter


def duplicate_encode(word):
    d = Counter(word.lower())
    new_word = ''
    for letter in word:
        if d[letter.lower()] > 1:
            new_word += ')'
        else:
            new_word += '('
    return new_word


words = ["din", "recede", "Success", '(( @'] #["(((", "()()()", ")())())", "))(("]
print(*(duplicate_encode(word) for word in words))