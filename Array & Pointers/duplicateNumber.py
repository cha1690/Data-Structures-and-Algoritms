class Solution:
    def duplicateNumber(self, nums):
        slow = fast = finder = 0
        while True:
            slow= nums[slow]
            fast = nums[nums[slow]]

            if fast == slow:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
