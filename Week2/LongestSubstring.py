class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #Brute Force Approach- O(n3), O(n)
        maxlength=0
        for i in range(len(s)):
            for j in range(i, len(s)):
                hashset=[]
                flag=0
                for k in range(i, j+1):
                    if s[k] in hashset:
                        flag=1
                        break
                    hashset.append(s[k])
                if flag ==0:
                    maxlength=max(maxlength, j-i+1)
        return maxlength

        # Two Pointer Approach-O(n), O(n)
        i = 0
        maxlength = 0
        hashset = []
        for j in range(len(s)):
            while s[j] in hashset:
                hashset.remove(s[i])
                i += 1
            hashset.append(s[j])
            maxlength = max(maxlength, j - i + 1)

        return maxlength