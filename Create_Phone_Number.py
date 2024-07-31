# task: https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    n = ''.join(map(str, n))
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # => returns "(123) 456-7890"