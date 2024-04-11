# You are given a large integer represented as an integer array digits, where each digits[i] is the ith
# digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plus_one(digits):
    n = 1
    num = 0
    for i in digits[::-1]:
        num += int(i) * n
        n *= 10

    return list(map(int, list(str(num + 1))))


def plus_one2(digits):
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))

print(plus_one2([1, 2, 3]))
print(plus_one2([8, 9, 9, 9, 9]))
