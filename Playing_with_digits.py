# task: https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    digits = map(int, str(n))
    total = sum([d ** ind for ind, d in enumerate(digits, p)])
    if total % n == 0:
        return total // n
    return -1