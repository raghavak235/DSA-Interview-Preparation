# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if  len(strs)==0:
            return [[""]]

        key_dict = {}
        for i in strs:
            sort_values = ''.join(sorted(i))
            # print(sort_values)
            if sort_values not  in key_dict:
                key_dict[sort_values]=[i]
            else:
                key_dict[sort_values].append(i)
        print(key_dict.values())
        return (key_dict.values())