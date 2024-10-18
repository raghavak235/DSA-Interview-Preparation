# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        key1 = {}
        slist = s.split()
        if len(slist) != len(patten):
            return False
        # print(slist)
        for i in range(len(pattern)):
            if pattern[i] not in key1:
                if slist[i] in key1.values():
                    return False
                key1[pattern[i]] = slist[i]
            elif key1[pattern[i]] != slist[i]:
                return False

        return True
