# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# def twoSum(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# Более быстрое решение с использованием хэш-таблицы
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 3], 6))
