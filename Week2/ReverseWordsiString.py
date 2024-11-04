# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_str = ''
        s_trim = str(s).strip().split()[::-1]
        print(s_trim)
        for i in s_trim:
            reversed_str += i
            reversed_str += ' '
        print(reversed_str)
        return reversed_str.strip()

