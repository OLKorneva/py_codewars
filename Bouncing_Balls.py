# task: https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        count = 1
        hight = h * bounce
        while hight > window:
            hight *= bounce
            count += 2
        return count
    return -1


print((bouncing_ball(3, 0.66, 1.5)))
print((bouncing_ball(3, 1, 1.5)))