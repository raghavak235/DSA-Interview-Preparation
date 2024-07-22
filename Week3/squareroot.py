https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150
# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        # Binary Search Implementation.
        low, high = 0, x//2
        while low <= high:
            mid = low +(high-low)//2
            value = mid * mid
            #Perfect Square
            if value == x:
                return mid
            elif x > value:
                low = mid + 1
            else:
                high = mid -1
        # Rounding to the nearest digit
        return high
