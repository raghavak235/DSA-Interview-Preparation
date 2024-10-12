# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i =0
        maxlength=0
        hashset=[]
        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i +=1
            hashset.append(s[j])
            maxlength=max(maxlength, j-i+1)

        return maxlength