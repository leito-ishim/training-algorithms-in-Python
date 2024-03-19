# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def valid_parentheses(s):
    if len(s) % 2 != 0:
        return False
    else:
        brackets_dict = {'(': ')', '{': '}', '[': ']'}
        temp_str = ''
        for i in s:
            if i not in brackets_dict.values():
                temp_str += brackets_dict.get(i)
            else:
                if len(temp_str) < 1 or i != temp_str[len(temp_str) - 1]:
                    return False
                else:
                    temp_str = temp_str[:-1]
        if len(temp_str) == 0:
            return True
        else:
            return False


print(valid_parentheses('()()'))
print(valid_parentheses('(())'))
print(valid_parentheses("(]"))
print(valid_parentheses("]]"))
print(valid_parentheses(")]"))
print(valid_parentheses('}}'))
print(valid_parentheses('{{'))

# def validParentheses(s):
#     if len(s) % 2 != 0:
#         return False
#     else:
#         # brackets_count_dict = {')': 0, '}': 0, ']': 0}
#         round_count = 0
#         square_count = 0
#         curly_count = 0
#         if s[0] in ['}', ')', ']']:
#             return False
#         for i in s:
#             if i == '(':
#                 round_count += 1
#             if i == '[':
#                 square_count += 1
#             if i == '{':
#                 curly_count += 1
#             if i == ')':
#                 if round_count < 1:
#                     return False
#                 else:
#                     round_count -= 1
#             if i == ']':
#                 if square_count < 1:
#                     return False
#                 else:
#                     square_count -= 1
#             if i == '}':
#                 if curly_count < 1:
#                     return False
#                 else:
#                     curly_count -= 1
#         return True
