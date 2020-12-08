# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
    if not strs:
        return ""

    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for string in strs:
            if string[i] != char:
                return shortest[:i]
    return shortest