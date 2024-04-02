# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'.
# Read this character in if it is either. This determines if the final result is negative or positive respectively.
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached.
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read,
# then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
# then clamp the integer so that it remains in the range. Specifically,
# integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


def myAtoi(s):
    result = ''
    for i in s:
        if i == ' ' and len(result) == 0:
            continue
        if (i == '+' or i == '-') and len(result) == 0:
            result += i
            continue
        if i.isdigit():
            result += i
        else:
            break
    try:
        num = int(result)
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num
    except ValueError:
        return 0


print(myAtoi("042"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("+ggg"))
print(myAtoi("-123456789658"))