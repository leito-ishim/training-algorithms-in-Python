# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


def longest_common_prefix(strs):
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans


print(longest_common_prefix(['flower', 'flow', 'flight']))
print(longest_common_prefix(['dog', 'racecar', 'car']))
print(longest_common_prefix(['']))
print(longest_common_prefix(['', '']))
print(longest_common_prefix(['dddd', 'ddddd']))
