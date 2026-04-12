class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 ={}
        for c in s:
            if(c in h1):
                h1[c] += 1
            else:
                h1[c] = 1
        h2 ={}
        for c in t:
            if(c in h2):
                h2[c] +=1
            else:
                h2[c] = 1
        for key in h1:
            if(key in h2):
                if(h1[key] != h2[key]):
                    return False
            else:
                return False
        if(len(h1) != len(h2)):
            return False

        return True

        