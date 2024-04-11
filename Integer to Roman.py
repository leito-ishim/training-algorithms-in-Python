# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number nine,
# which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.


def getRomanNum(num, arr):
    match num:
        case 1: return arr[0]
        case 2: return arr[0] * 2
        case 3: return arr[0] * 3
        case 4: return arr[0] + arr[1]
        case 5: return arr[1]
        case 6: return arr[1] + arr[0]
        case 7: return arr[1] + arr[0] * 2
        case 8: return arr[1] + arr[0] * 3
        case 9: return arr[0] + arr[2]
        case _: return ''


def intToRoman(num):
    template = {
        1: ['I', 'V', 'X'],
        2: ['X', 'L', 'C'],
        3: ['C', 'D', 'M'],
        4: ['M'],
    }
    result = ''
    count = 1
    while num > 0:
        result = getRomanNum(num % 10, template.get(count)) + result
        num = num // 10
        count += 1
    return result


print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))