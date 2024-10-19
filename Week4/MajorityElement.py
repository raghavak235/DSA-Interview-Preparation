# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Boyer and Moore Voting Algorithm
        #  Time Complexity: O(n)
        #  Space Complexity: O(1)

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num

            count += (1 if candidate == num else -1)
        return candidate