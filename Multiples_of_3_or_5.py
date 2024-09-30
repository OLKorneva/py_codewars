# task: https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    res = 0
    for i in range(number):
        if i % 3 == 0:
            res += i
        elif i % 5 == 0:
            res += i
    return res

Multiples_of_3_or_5.py 
print(solution(-1))


