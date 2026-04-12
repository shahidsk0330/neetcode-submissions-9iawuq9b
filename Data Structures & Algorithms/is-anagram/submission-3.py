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
        for key in s_occ:
            if key in t_occ:
                if t_occ[key] != s_occ[key]:
                    return False
            else:
                return False
        return True
        