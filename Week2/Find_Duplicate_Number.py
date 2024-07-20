# Floyd's Cycle Detection Algorithm
#Time Complexity: O(n)
#Space Complexity: O(1)
https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = nums[0]
        
        ## Part 1: find the meeting point of the 2 pointers[slow and fast)
        while True:
            # one step at a time
            slow = nums[slow]
            # Two step at a time
            fast= nums[nums[fast]]
            # Meeting Point
            if slow == fast:
                break

        slow = nums[0]
        # Part 2: find the starting point/entrance of the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
