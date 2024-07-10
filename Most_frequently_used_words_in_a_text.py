#task: https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

from collections import Counter
import re
def top_3_words(text):
    #ls_text = re.findall(r"(?:(?<=^)|(?<=[^'a-zA-Z]))([a-zA-Z]+'[a-zA-Z]+|[a-zA-Z]+|[a-zA-Z]+'|'[a-zA-Z]+)+(?=[^'a-zA-Z]|$)", text.lower())
    #ls_text = re.findall(r"(?:(?<=^)|(?<=[^'a-zA-Z]))([a-zA-Z]+'[a-zA-Z]+)+(?=[^'a-zA-Z]|$)",text.lower())
    ls_text = re.split(r"[^'a-zA-Z]", text.lower())
    ls_text = [el for el in ls_text if el != '' and re.search(r'[a-zA-Z]', el)]
    dict_text = Counter(ls_text)
    return list(i[0] for i in sorted(dict_text.items(), key=lambda x: x[1], reverse=True)[:3])

text = '''In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.''' #["a", "of", "on"]

#text = "a a a  b  c c  d d d d  e e e e e" #["e", "d", "a"]

#text = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e" # ["e", "ddd", "aa"]

#text = "  //wont won't won't " # ["won't", "wont"]

#text = "  , e   .. " # ["e"]

#text = "  ...  " #[]

#text = "  '  " # []

#text = "  '''  " # []

print(top_3_words(text))


'''
Interesting solution:

from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]
'''