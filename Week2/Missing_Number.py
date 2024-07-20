https://leetcode.com/problems/missing-number/description/
#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        xor1=0
        for i in range(1,n+1):
            xor1 = xor1 ^ i

        for i in range(n):
            xor1 ^= nums[i]

        print(xor1)
        return xor1
