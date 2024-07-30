# task: https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python


def find_even_index(arr):
    left, right = 0, sum(arr)
    for ind, num in enumerate(arr):
        if left == right - num:
            return ind
        left += num
        right -= num
    return -1

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10, -10]))
print(find_even_index([-3, 2, 1, 0]))
# test.assert_equals(find_even_index([10, -10]), -1)
# test.assert_equals(find_even_index([-3, 2, 1, 0]), 3)