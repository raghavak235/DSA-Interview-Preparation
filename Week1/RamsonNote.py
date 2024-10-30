# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count={}
        for i in magazine:
            if i in count:
                count[i] +=1
            else:
                count[i] =1

        for j in ransomNote:
            if j not in count or count[j]==0:
                return False
            else:
                count[j] -=1
        # print(count)
        return True

        # return True if ransomNote in magazine else False