# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


def reverse(x):
    num = int(str(x)[::-1]) if str(x)[0] != '-' else int('-'+(str(x)[1::])[::-1])
    return num if abs(num) < 2**31 and num != 2**31 - 1 else 0



print(reverse(1534236469))
print(reverse(-123))

