# task: https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

def get_pins(observed):
    data = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'],
            '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'],
            '8': ['5', '7', '8', '9', '0'], '9': ['6', '8', '9'], '0': ['8', '0']}
    res = []
    for dig in observed:
        if not res:
            res = data[dig]
        else:
            res = [i + j for i in res for j in data[dig]]
    return res

print(get_pins('8'))
print(get_pins('11'))
print(get_pins('369'))