# task: https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):
    words = sentence.split()
    res = [''] * len(words)
    for word in words:
        for letter in word:
            if letter in '1234567890':
                res[int(letter) - 1] = word
                break
    return ' '.join(res)


print(order("is2 Thi1s T4est 3a"))