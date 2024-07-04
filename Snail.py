# task: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def snail(snail_map):
    n = len(snail_map)
    res = []
    if not snail_map or type(snail_map) is not list or len(snail_map[0]) == 0:
        return res
    directions = ('right', 'down', 'left', 'up')
    ind_direction = 0
    i, j = 0, 0
    for _ in range(n ** 2):
        res.append(snail_map[i][j])
        snail_map[i][j] = None
        if directions[ind_direction] == 'right':
            j += 1
            if not (j + 1 < n and snail_map[i][j + 1]):
                ind_direction += 1
        elif directions[ind_direction] == 'down':
            i += 1
            if not (i + 1 < n and snail_map[i + 1][j]):
                ind_direction += 1
        elif directions[ind_direction] == 'left':
            j -= 1
            if not (0 <= j - 1 and snail_map[i][j - 1]):
                ind_direction += 1
        elif directions[ind_direction] == 'up':
            i -= 1
            if not (0 <= i - 1 and snail_map[i - 1][j]):
                ind_direction = 0

    return res

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # => [1,2,3,6,9,8,7,4,5]
#array = [[]]
print(snail(array))

'''
interesting decision:

def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

'''