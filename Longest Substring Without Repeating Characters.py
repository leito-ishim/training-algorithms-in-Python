# Given a string s, find the length of the longest substring  without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1 or len(s) == len(set(s)):
            return len(s)
        rezult = []
        temp_str = s[0]
        for i in range(1, len(s)):
            if s[i] not in temp_str:
                temp_str += s[i]
            else:
                rezult.append(len(temp_str))
                temp_str = temp_str[temp_str.index(s[i]) + 1:] + s[i]
            print(temp_str)
        rezult.append(len(temp_str))
        # print(rezult)
        return max(rezult)



# print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("bbbbb"))
# print(Solution().lengthOfLongestSubstring("pwwkew"))
# print(Solution().lengthOfLongestSubstring("au"))
# print(Solution().lengthOfLongestSubstring("aab"))
print(Solution().lengthOfLongestSubstring("dvdf"))
