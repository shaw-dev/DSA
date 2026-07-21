class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        string ={"+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b)}
        # string =["+", 
        #          "-",
        #          "*", 
        #          "/"]

        stack=[]
        
        ans =0
        for char in tokens:
            if char not in string :
                stack.append(int(char))
            elif char in string:
                right= stack.pop()
                left = stack.pop()
                result = string[char](left,right)
                stack.append(result)
            
        return stack[-1]

            
