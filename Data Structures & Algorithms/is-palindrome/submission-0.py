class Solution:
    def isPalindrome(self, s: str) -> bool:
        u =""
        for c in s:
            if c.isalnum():
                u+=c.lower()
        l,r=0,len(u)-1
        print(u)
        while(l<r):
            if(u[l] != u[r]):
                return False
            l+=1
            r-=1
        return True
        
        