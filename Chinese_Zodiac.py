# task: https://www.codewars.com/kata/57a73e697cb1f31dd70000d2/train/python


animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
elements = ["Wood", "Fire", "Earth", "Metal", "Water"]


def chinese_zodiac(year):
    ind = (year - 1924) % 60
    return ' '.join([elements[ind // 2 % 5], animals[ind % 12]])

print(chinese_zodiac(1998))
