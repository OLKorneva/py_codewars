# task: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python


def reverse_words(text):
    res = []
    word = []
    for s in text:
        if s == ' ':
            if word:
                res.append(''.join(word[::-1]))
                word = []
            res.append(s)
        else:
            word.append(s)
    if word:
        res.append(''.join(word[::-1]))
    return ''.join(res)

