class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""
        for char in s: 
            if char.isalnum():
                alpha +=char.lower()
        start, end = 0, len(alpha)-1
        
        while start < end: 
            if alpha[start] != alpha[end]:
                return False
            start +=1
            end -=1
        return True

        

        