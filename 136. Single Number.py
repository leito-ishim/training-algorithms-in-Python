# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# def singleNumber(nums):
#     total = 0
#     for num in nums:
#         total ^= num
#     return total

def singleNumber(nums):
    hash = {}

    for num in nums:
        hash[num] = hash.get(num, 0) + 1

    for i in hash:
        if hash[i] == 1:
            return i


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
