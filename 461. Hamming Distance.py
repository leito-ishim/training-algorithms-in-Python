# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.
# Example 1:
#
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# def hammingDistance(x, y):
#     x_bin = bin(x)[2:]
#     y_bin = bin(y)[2:]
#     if len(x_bin) > len(y_bin):
#         y_bin = y_bin.zfill(len(x_bin))
#     else:
#         x_bin = x_bin.zfill(len(y_bin))
#     count = 0
#     for i in range(len(x_bin)):
#         if x_bin[i] != y_bin[i]: count += 1
#     return count

def hammingDistance(x, y):
    return bin(x^y).count('1')


print(hammingDistance(1, 4))
print(hammingDistance(3, 1))