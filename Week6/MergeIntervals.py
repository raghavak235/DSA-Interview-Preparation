# https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort it based on the start time
        intervals.sort(key=lambda i: i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            # Previous Interval Constraint
            previousIntervalEnd = result[-1][1]
            # Over lapping intervaals
            if start <= previousIntervalEnd:
                result[-1][1] = max(previousIntervalEnd, end)
            else:
                result.append([start, end])

        return result