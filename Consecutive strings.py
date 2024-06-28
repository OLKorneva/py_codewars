# task: https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    if len(strarr) >= k > 0 and len(strarr) > 0:
        res = [''.join(strarr[i - k:i]) for i in range(k, len(strarr) + 1)]
        return max(res, key=len)
    return ''

