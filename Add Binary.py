# Given two binary strings a and b, return their sum as a binary string.


# def strBinToInt(s):
#     return sum(int(s[len(s)-i-1]) * (2 ** i) for i in range(len(s)))
#
#
# def addBinary(a, b):
#     return bin(strBinToInt(a)+strBinToInt(b))[2:]


def addBinary(a, b):
    return format((int(a, 2)+int(b, 2)), 'b')

# print(strBinToInt('110'))
# print(strBinToInt('10010010'))
print(addBinary('11', '1'))
print(addBinary('1010', '1011'))
