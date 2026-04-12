class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        length =1
        for L in range(len(s)):
            for R in range(L+1,len(s)):
                if(s[R] in s[L:R]):
                    break
                else:
                    print(length)
                    length = max(length, R-L+1)
        return length
        