# task: https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    width = 1 + 2 * (n_floors - 1)
    return [' ' * i + '*' * num + ' ' * i for i, num in enumerate(range(width, -1, -2))][::-1]


print(*[row for row in tower_builder(6)], sep='\n')
