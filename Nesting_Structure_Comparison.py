#task: https://www.codewars.com/kata/520446778469526ec0000001/train/python


def same_structure_as(original, other):
    if isinstance(original, list) is not True or isinstance(other, list) is not True:
        return False
    if len(other) != len(original):
        return False
    for first, second in zip(original, other):
        if (isinstance(first, list) is True and isinstance(second, list) is False or
                isinstance(first, list) is False and isinstance(second, list) is True):
            return False
        if isinstance(first, list):
            if len(first) != len(second):
                return False
            if not same_structure_as(first, second):
                return False
    return True


# should return True
print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))

# should return False
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))

# should return True
print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))