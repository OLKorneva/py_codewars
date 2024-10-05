# task: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    ind = []
    nums = []
    for i, n in enumerate(source_array):
        if n % 2 == 1:
            ind.append(i)
            nums.append(n)
    for i, n in zip(ind, sorted(nums)):
        source_array[i] = n

    return source_array


print(sort_array([7, 1])) # =>  [1, 7]
print(sort_array([5, 8, 6, 3, 4])) #  =>  [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) #  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]