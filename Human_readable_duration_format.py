# task: https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    years = (seconds // (60 * 60 * 24 * 365), 'years')
    days = (seconds % (60 * 60 * 24 * 365) // (60 * 60 * 24), 'days')
    hours = (seconds % (60 * 60 * 24 * 365) % (60 * 60 * 24) // (60 * 60), 'hours')
    minutes = (seconds % (60 * 60 * 24 * 365) % (60 * 60 * 24) % (60 * 60) // 60, 'minutes')
    secs = (seconds % (60 * 60 * 24 * 365) % (60 * 60 * 24) % (60 * 60) % 60, 'seconds')
    ls = [years, days, hours, minutes, secs]
    res = []
    for duration in ls:
        if duration[0] == 0:
            continue
        if duration[0] == 1:
            res.append(f'1 {duration[1][:-1]}')
        else:
            res.append(f'{duration[0]} {duration[1]}')
    res = ', '.join(res)
    if ',' in res:
        res = res[::-1].replace(',', 'dna ', 1)[::-1]
    return res


print(format_duration(132030240))