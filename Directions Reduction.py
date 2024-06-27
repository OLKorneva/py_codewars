#task: https://www.codewars.com/kata/550f22f4d758534c1100025a

def dir_reduc(arr):
    s1, s2 = set(["NORTH", "SOUTH"]), set(["EAST", "WEST"])
    while True:
        flag = False
        for i in range(1, len(arr)):
            tm = {arr[i - 1], arr[i]}
            if tm == s1 or tm == s2:
                arr = arr[:i - 1] + arr[i + 1:]
                break
            if i == len(arr) - 1:
                flag = True
        if flag or len(arr) <= 1:
            break
    return arr

