# https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is the same forwards and backwards
        return cleaned == cleaned[::-1]


    # The difference between isalpha() and isalnum() in Python lies in what characters they consider as valid:
    #
    # isalpha():
    #
    # Returns True if all characters in the string are alphabetic (letters) and there is at least one character, otherwise False.
    # Only letters (both uppercase and lowercase) are considered valid.
    # Example:
    # python
    # Copy code
    # "abc".isalpha()    # True
    # "abc123".isalpha() # False
    # "123".isalpha()    # False
    # isalnum():
    #
    # Returns True if all characters in the string are alphanumeric (letters or numbers) and there is at least one character, otherwise False.
    # Both letters and digits are considered valid.
    # Example:
    # python
    # Copy code
    # "abc".isalnum()    # True
    # "abc123".isalnum() # True
    # "123".isalnum()    # True
    # "abc!".isalnum()   # False
    # In the palindrome-checking problem, isalnum() is the appropriate choice because we want to keep both letters and numbers in the filtered string.