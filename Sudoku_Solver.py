# task: https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    d_empty = {(i, j): list(range(1, 10)) for i in range(9) for j in range(9) if puzzle[i][j] == 0}
    while d_empty:
        for x, y in d_empty:
            for i in range(9):
                if puzzle[i][y] in d_empty[(x, y)]:
                    d_empty[(x, y)].remove(puzzle[i][y])
                if puzzle[x][i] in d_empty[(x, y)]:
                    d_empty[(x, y)].remove(puzzle[x][i])
            for i in range(3 * (x // 3), 3 * (x // 3) + 3):
                for j in range(3 * (y // 3), 3 * (y // 3) + 3):
                    if puzzle[i][j] in d_empty[(x, y)]:
                        d_empty[(x, y)].remove(puzzle[i][j])
        keys = []
        for key, value in d_empty.items():
            if len(value) == 1:
                x, y = key
                puzzle[x][y] = value[0]
                keys.append(key)

        for key in keys:
            d_empty.pop(key)

    return puzzle



puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))

'''
Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
'''





