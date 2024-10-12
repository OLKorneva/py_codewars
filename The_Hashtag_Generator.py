# task: https://www.codewars.com/kata/52449b062fb80683ec000024/train/python


def generate_hashtag(s):
    if not s:
        return False
    res = '#' + ''.join([word.capitalize() for word in s.split()])
    if len(res) > 140 or not res[1:]:
        return False
    return res


print(generate_hashtag(" Hello there thanks for trying my Kata")) #  =>  "#HelloThereThanksForTryingMyKata"
print(generate_hashtag("    Hello     World   ")) #                  =>  "#HelloWorld"
print(generate_hashtag("")) #                                        =>  false