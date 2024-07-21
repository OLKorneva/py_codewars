#task: https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

def area_or_perimeter(l, w):
    return l ** 2 if l == w else 2 * (l + w)

print(area_or_perimeter(2, 3))