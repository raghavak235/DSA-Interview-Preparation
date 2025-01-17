Time Complexity: O(n3)
Generating all substrings takes O(n2)
Checking each substring for uniqueness in the simplest way is O(n)
Because we must at least iterate over all characters in that substring to see if they are all distinct—this iteration is 
O(k) where  k is the substring length (up to n)
Space Complexity: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len =0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]

                # Verfying no deuplicates and adding to the length
                if len(set(substring))==len(substring):
                    max_len = max(max_len,j-i+1)
            
        return max_len


Time Complexity: it appears O(n2). So, across the entire run of the algorithm, no character gets added or removed more than once. This yields total of O(n) + O(n)
Space Complexity: O(n)



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()   # holds the characters in the current window
        l = 0              # left pointer of the window
        max_len = 0        # result to keep track of the max length

        for r in range(len(s)):
            # While the current character is already in the set,
            # move the left pointer to shrink the window until
            # the character can be added without duplication.
            while is used because you may need to keep removing characters from the left pointer multiple times until the window is free of the character you are about to add.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Now it's safe to add s[r] because it's guaranteed
            # not to be in the set anymore
            char_set.add(s[r])
            
            # Update max_len with the size of the current window
            window_size = r - l + 1
            max_len = max(max_len, window_size)

        return max_len
