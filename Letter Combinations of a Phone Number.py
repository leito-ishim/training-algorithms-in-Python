# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]

# def letterCombinations(digits):
#     digitsDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#     if not digits: return ''
#     result = []
#     for i in range(len(digits)):
#         result = sorted(result * len(digitsDict.get(digits[i])))
#         if i == 0:
#             for j in digitsDict.get(digits[i]):
#                 result.append(j)
#         else:
#             count = 0
#             for j in range(len(result)):
#                 if count == len(digitsDict.get(digits[i])):
#                     count = 0
#                 result[j] = result[j] + digitsDict.get(digits[i])[count]
#                 count += 1
#     return result

# Решение через рекурсию
def letterCombinations(digits):
    if not digits: return ''
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            result.append(combination)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    backtrack('', digits)
    return result


print(letterCombinations('23'))
print(letterCombinations(''))
print(letterCombinations('2'))
