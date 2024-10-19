# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_mapping = {'(':')','[':']','{':'}'}
        open_brackets=set(['(','[','{'])
        stack=[]
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif stack and i == bracket_mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack==[]