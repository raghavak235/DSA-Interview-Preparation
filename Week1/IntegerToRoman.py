# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman =''
        i=0
        while num>0:
            div = num//values[i]
            num=num%values[i]
            while div:
                roman = roman+symbols[i]
                div=div-1
            i = i+1
        return roman
