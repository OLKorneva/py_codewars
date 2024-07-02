# task: https://www.codewars.com/kata/5503013e34137eeeaa001648

def diamond(n):
    if n > 0 and n % 2 == 1:
        res = []
        for i in range(1, n - 1, 2):
            num_space = (n - i) // 2
            res.append(' ' * num_space + '*' * i)
        res = res + ['*' * n] + res[::-1]
        return '\n'.join(res) + '\n'


print(diamond(3))