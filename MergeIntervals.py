# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

class Solution:
    def mergeIntervals(self,intervals):
        result = [intervals[0]]
        intervals.sort()
        for i in range(1, len(intervals)):
            if res[-1][1] >= interval[i][0]:
                res[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result