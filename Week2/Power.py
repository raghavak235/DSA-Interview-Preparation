https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

# Time Complexity: O(logn)
# Space Complexity: O(logn64)= 7 to 8 stack spaces

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        elif n ==1:
            return x
        
        elif n <0:
            x=1/x
            n=-n
            
            return self.myPow(x,n)
        else:
            # Divide and Conquer Method
            mid=n//2
            result=self.myPow(x,mid)
            finalresult =  result * result
            if n % 2 == 0:
                return finalresult
            else:
                return x * finalresult


        
