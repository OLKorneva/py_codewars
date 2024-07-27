# task: https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    res = None
    for item in recipe:
        num = available.get(item)
        if num:
            tm_res = num // recipe[item]
            if not res or res > tm_res:
                res = tm_res
        else:
            return 0
    return res if res is not None else 0


# must return 2
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
# must return 0
print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))
