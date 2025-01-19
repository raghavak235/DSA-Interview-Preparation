class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        result=0
        start=0
        n = len(s)
        for i in range(0, n-k+1):
                string = s[i:i+k]
                print(string)
                if len(set(string))==3:
                    result += 1
        # print((result))
        return result
