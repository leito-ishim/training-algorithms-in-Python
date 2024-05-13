# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# def convertToTitle(columnNumber):
#     numbers = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
#                13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W',
#                24: 'X', 25: 'Y', 0: 'Z'}
#     res = ''
#     while columnNumber > 26:
#         a = columnNumber % 26
#         res = numbers[a] + res
#         if a != 0:
#             columnNumber //= 26
#         else:
#             columnNumber = columnNumber // 26 - 1
#
#     return numbers[columnNumber % 26] + res
#


def convertToTitle(columnNumber):
    res = ''
    while columnNumber > 0:
        res = chr(ord('A') + (columnNumber - 1) % 26) + res
        columnNumber = (columnNumber - 1) // 26
    return res


print(convertToTitle(26))
print(convertToTitle(27))
print(convertToTitle(28))
print(convertToTitle(52))
print(convertToTitle(701))

print(chr(ord('A')))
