
# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        T = len(t)

        if s == '': return True
        if S > T: return False

        j_s = 0
        for i in range(T):
            if t[i] == s[j_s]:
                if j_s == S - 1:
                    return True
                j_s += 1
        return False