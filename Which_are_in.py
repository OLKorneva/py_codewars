# task: https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python


def in_array(array1, array2):
    '''
    res = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                res.append(word1)
                break

    return sorted(set(res))
    '''
    return sorted(set([word1 for word1 in array1 for word2 in array2 if word1 in word2]))

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2)) #returns ["arp", "live", "strong"]


a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2)) #returns []