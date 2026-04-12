class Solution:
    def isValid(self, s: str) -> bool:
        o =["(","[","{"]
        res =["()","{}","[]"]
        stack =[]
        for bra in s:
            if(bra in o):
                stack.append(bra)
            else:
                if stack:
                    x = stack.pop()
                    if x + bra not in res:
                        return False
                else:
                    return False
        return True if len(stack)==0 else False
    

        

        