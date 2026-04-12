class Solution:
    def palindrome(self, s) -> bool: 
        left, right = 0, len(s)-1
        while left < right: 
            if (s[left] == s[right]):
                left +=1
                right -=1
            else: 
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            v =s[:i]+s[i+1:]
            if self.palindrome(v):
                return True
        return False
        



            

        