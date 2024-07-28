# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original_num=x
        reversed_num=0
        while original_num>0:

            # Last digit in number
            digit = original_num % 10

            #Adding the digit to this number
            reversed_num = reversed_num * 10 + digit

            # Removing the digit
            original_num = original_num // 10


        if x == reversed_num:
            return True
        else:
            return False
