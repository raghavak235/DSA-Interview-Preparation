# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        d2={}
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if c1 in d1 and d1[c1]!=c2:
                return False
            elif c2 in d2 and d2[c2]!=c1:
                return False
            else:
                d1[c1]=c2
                d2[c2]=c1

        return True