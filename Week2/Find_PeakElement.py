https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150
# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums) 
        low, high = 0, n-1

        if n==1:
            return 0
       
       #Binary Search Implementation:
        while low <=high:
            mid = low+(high-low)//2
            if (mid == 0 and nums[mid] > nums[mid + 1]) or (mid == n-1 and nums[mid]>nums[mid-1]) or (nums[mid] > nums[mid+1] and nums[mid]> nums[mid-1]):

                return mid
            elif nums[mid] <nums[mid+1]:
                low = mid +1
            else:
                high = mid-1
            
