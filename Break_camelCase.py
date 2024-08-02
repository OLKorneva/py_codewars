#task: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
    return ''.join([sym if sym.islower() else f' {sym}' for sym in s])


print(solution(''))

