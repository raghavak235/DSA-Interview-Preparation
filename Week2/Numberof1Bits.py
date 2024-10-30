# https://leetcode.com/problems/number-of-1-bits/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(int(n))
        # print(binary)
        count = 0
        for i in binary:
            print(type(i))
            if i == '1':
                count += 1
        return count
