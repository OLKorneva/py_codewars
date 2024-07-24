# task: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(s):
    res = ''
    for sym in s:
        if s.lower().count(sym.lower()) == 1:
            res = sym
            break
    return res


words = ['a', 'stress', 'sTrass', 'moonmen']

print(*[first_non_repeating_letter(w) for w in words])