# https://leetcode.com/problems/happy-number/submissions/1426289821/

class Solution(object):
    def sumofsquares(seelf, n):
        sum = 0
        while n > 0:
            last_digit = n % 10
            sum += last_digit * last_digit
            n = n // 10
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumofsquares(n)
            if n == 1:
                return True

        return False

