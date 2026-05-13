class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two words are not equal length: return False
        if len(s) != len(t):
            return False
        for c in s: 
            if s.count(c) != t.count(c):
                return False
        return True
