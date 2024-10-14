# task: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python


def increment_string(strng):
    nums = []
    count = 0
    for item in strng[::-1]:
        if item.isdigit():
            count += 1
            nums.append(item)
        else:
            break
    if nums:
        return strng[:len(strng) - count] + str(int(''.join(nums[::-1])) + 1).zfill(len(nums))
    return strng + '1'



print(increment_string('foo')) #-> foo1
print(increment_string('foobar23')) #-> foobar24
print(increment_string('foo0042')) #-> foo0043
print(increment_string('foo9')) #-> foo10
print(increment_string('foo099')) #-> foo100