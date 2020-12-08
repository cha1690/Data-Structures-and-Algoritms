# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

def strStr(haystack, needle):
    for index in range(len(haystack)-len(needle)+1):
        if haystack[index:index+len(needle)] == needle:
            return index
        return -1
