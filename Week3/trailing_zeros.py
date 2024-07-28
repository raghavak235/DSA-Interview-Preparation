#Time Complexity: O(logn)
#Space Complexity: 0(1)

# we need to find the number of 5's in the number
# The formula for the counts of 5's in the prime factor of n!= floor(n/5) + floor(n/25) + ----

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=0
        while n>0:
            x = n//5
            result += n//5
            n=x
        return result

    
