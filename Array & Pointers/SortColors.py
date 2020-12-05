# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Follow up:
#
# Could you solve this problem without using the library's sort function?
# Could you come up with a one-pass algorithm using only O(1) constant space?

class Solution:
    def sortColors(self,arr):
        left, right, curr_index = 0, len(arr)-1, 0

        while curr_index<= right:
            if arr[curr_index] == 0:
                arr[curr_index], arr[left] = arr[left], arr[curr_index]
                curr_index+=1
                left+=1
            elif arr[curr_index] == 2:
                arr[curr_index], arr[right] = arr[right], arr[curr_index]
                right-=1
            else:
                curr_index+=1
        return arr