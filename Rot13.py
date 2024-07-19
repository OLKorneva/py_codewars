# task: https://www.codewars.com/kata/530e15517bc88ac656000716

from string import ascii_lowercase, ascii_uppercase


def rot13(message):
    res = ''
    for let in message:
        if let in ascii_lowercase:
            ind = ascii_lowercase.index(let)
            new_ind = (ind + 13) % len(ascii_lowercase)
            res += ascii_lowercase[new_ind]
        elif let in ascii_uppercase:
            ind = ascii_uppercase.index(let)
            new_ind = (ind + 13) % len(ascii_uppercase)
            res += ascii_uppercase[new_ind]
        else:
            res += let
    return res