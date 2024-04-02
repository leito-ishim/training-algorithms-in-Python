# Given a string s, return the longest palindromic substring  in s
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# class Solution:
#
#     def isPalindrome(self, s: str) -> bool:
#         if len(s) % 2 == 0:
#             if s[:len(s) // 2:] == s[:len(s) // 2 - 1:-1]:
#                 return True
#         else:
#             if s[:len(s) // 2:] == s[:len(s) // 2:-1]:
#                 return True
#         return False
#
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1:
#             return s
#         rezult = {}
#         for i in range(len(s)):
#             s_copy = s[i:]
#             while len(s_copy) > 1:
#                 if s_copy[0] == s_copy[-1]:
#                     if self.isPalindrome(s_copy):
#                         rezult[len(s_copy)] = s_copy
#                     s_copy = s_copy[:-1]
#                 else:
#                     s_copy = s_copy[:-1]
#         return rezult.get(max(rezult.keys())) if rezult else s[0]
#         # return rezult.get(max(rezult.keys()))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]


# a = 'acbca'
# print(a[0])
# print(a[-1])
print(Solution().longestPalindrome("acbca"))
print(Solution().longestPalindrome("aacabdkacaa"))
