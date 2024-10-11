# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1419158698/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # If the array is empty, return 0

        i = 0  # Slow pointer

        # Start the fast pointer from index 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1  # Increment the slow pointer
                nums[i] = nums[j]  # Copy the unique element to the new position

        return i + 1  # Return the length of the unique portion of the array
