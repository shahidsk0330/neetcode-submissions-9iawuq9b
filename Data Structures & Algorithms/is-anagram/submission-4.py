class Solution:
    def count_characters(self,s): 
        occ = {}
        for char in s: 
            if char in occ: 
                occ[char] +=1
            else: 
                occ[char] = 1
        return occ
    def isAnagram(self, s: str, t: str) -> bool:
        s_occ = self.count_characters(s)
        t_occ = self.count_characters(t)
        if len(s_occ) != len(t_occ):
            return False
        return s_occ == t_occ
        