class Solution:
    def countWords(self, s):
        count = {}
        for c in s:
            if c in count: 
                count[c]+=1
            else:
                count[c] = 1
        return count
            
    def isAnagram(self, s: str, t: str) -> bool:
        s_count =self.countWords(s)
        t_count= self.countWords(t)
        if s_count == t_count:
            return True
        return False
       
        
        