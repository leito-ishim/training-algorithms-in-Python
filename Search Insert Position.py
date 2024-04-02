# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, nums, target):
        end_element = len(nums) - 1
        start_element = 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while start_element <= end_element:
            middle_element = start_element + (end_element - start_element) // 2
            if nums[middle_element] == target:
                return middle_element
            elif nums[middle_element] < target:
                start_element = middle_element + 1
            else:
                end_element = middle_element - 1
        return middle_element if target < nums[middle_element] else middle_element + 1


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 0))
print(Solution().searchInsert([1, 3, 5, 6], 2))
