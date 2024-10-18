#task: https://www.codewars.com/kata/58bee820e9f98b215200007c/train/python


def select(memory):
    hated_names = []
    memory = memory.split(', ')
    for i, name in enumerate(memory):
        if name[0] == '!':
            hated_names.extend((name, name[1:]))
            if i + 1 < len(memory):
                hated_names.append(memory[i+1])
    res = []
    for name in memory:
        if name not in hated_names:
            res.append(name)
    return ', '.join(res)


print(select("Albert Einstein, !Sarah Connor, Marilyn Monroe, Abraham Lincoln, Sarah Connor, Sean Connery, Marilyn Monroe, Bjarne Stroustrup, Manson Marilyn, Monroe Mary"))
#"Albert Einstein, Abraham Lincoln, Sean Connery, Bjarne Stroustrup, Manson Marilyn, Monroe Mary"