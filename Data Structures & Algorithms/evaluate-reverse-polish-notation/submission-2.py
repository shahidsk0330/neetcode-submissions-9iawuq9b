class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for ele in tokens:
            if ( ele not in operators):
                stack.append(int(ele))
            else:
                ele2 = stack.pop()
                ele1 = stack.pop()
                if ele == "+":
                    stack.append(ele1+ ele2)
                elif ele =="-":
                    stack.append(ele1-ele2)
                elif ele =="*":
                    stack.append(ele1*ele2)
                else:
                    stack.append(int(ele1/ele2))
        return stack[-1]
        