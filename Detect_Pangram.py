# task https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

from string import ascii_lowercase


def is_pangram(st):
    return set(ascii_lowercase) <= set(st.lower())

pangrams = [ "The quick brown fox jumps over the lazy dog.",
                     "Cwm fjord bank glyphs vext quiz",
                     "Pack my box with five dozen liquor jugs.",
                     "How quickly daft jumping zebras vex.",
                     "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ" ]
for pangram in pangrams:
    print(is_pangram(pangram))

print()

non_pangrams = [ "This isn't a pangram!",
                         "abcdefghijklm opqrstuvwxyz",
                         "Aacdefghijklmnopqrstuvwxyz" ]
for non_pangram in non_pangrams:
    print(is_pangram(non_pangram))