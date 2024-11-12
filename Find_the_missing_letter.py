#task: https://www.codewars.com/kata/5839edaa6754d6fec10000a2/solutions/python


def find_missing_letter(chars):
    ind = None
    for letter in chars:
        if ind:
            if ord(letter) - ind == 1:
                ind = ord(letter)
            else:
                return chr(ord(letter) - 1)
        else:
            ind = ord(letter)

