class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words ={}
        for c in s:
            if c in words:
                words[c] +=1
            else:
                words[c] = 1
        wordt ={}
        for c in t:
            if c in wordt:
                wordt[c] +=1
            else:
                wordt[c] =1
        for key in words:
            if key in wordt:
                if(words[key] != wordt[key]):
                    return False
            else:
                return False
        if len(words) != len(wordt):
            return False
        return True
        
