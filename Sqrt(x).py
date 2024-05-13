# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


def mySqrt(x):
    if x ** 2 == x:
        return x
    min = 0
    max = x
    while True:
        temp = (min + max) // 2
        if temp ** 2 <= x and (temp + 1) ** 2 > x:
            return temp
        if temp ** 2 < x and (temp + 1) ** 2 <= x:
            min = temp
        elif temp ** 2 > x:
            max = temp


print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(25))
