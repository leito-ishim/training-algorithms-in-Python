# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


def convert(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    result = [''] * numRows
    dir = 'down'
    line = 0
    for i in range(len(s)):
        result[line] += s[i]
        if line + 1 == numRows and dir == 'down':
            dir = 'up'
        elif line == 0 and dir == 'up' and i > 0:
            dir = 'down'
        if dir == 'down':
            line += 1
        elif dir == 'up':
            line -= 1
    return ''.join(result)


print(convert('PAYPALISHIRING', 3))
