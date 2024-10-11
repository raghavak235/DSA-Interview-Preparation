# https://leetcode.com/problems/remove-element/submissions/1418634028/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

