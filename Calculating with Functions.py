# task: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

from operator import add, mul, sub, floordiv
def number(digit, f=None):
    if f is not None:
        return f(digit)
    else:
        return digit

def zero(f=None): return number(0, f)
def one(f=None): return number(1, f)
def two(f=None): return number(2, f)
def three(f=None): return number(3, f)
def four(f=None): return number(4, f)
def five(f=None): return number(5, f)
def six(f=None): return number(6, f)
def seven(f=None): return number(7, f)
def eight(f=None): return number(8, f)
def nine(f=None): return number(9, f)

def operate(op, *nums):
    if len(nums) == 2:
        return op(nums[0], nums[1])
    elif len(nums) == 1:
        return lambda x: op(x, nums[0])

def plus(*nums): return operate(add, *nums)
def minus(*nums): return operate(sub, *nums)
def times(*nums): return operate(mul, *nums)
def divided_by(*nums): return operate(floordiv, *nums)

print(seven(times(five())), four(plus(nine())), eight(minus(three())), six(divided_by(two()))) # must return 3