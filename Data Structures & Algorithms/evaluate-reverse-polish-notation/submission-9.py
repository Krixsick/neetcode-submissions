class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token not in ("*", "/", "+", "-"):
                stack.append(int(token))
            else:
                e1 = int(stack.pop())
                e2 = int(stack.pop())
                tmp = 0 
                if token == "+":
                    tmp = e2 + e1 
                elif token == "-":
                    tmp = e2 - e1
                elif token == "*":
                    tmp = e2 * e1
                else:
                    tmp = e2 / e1
                stack.append(int(tmp))
        return stack[-1] if stack else int(tokens[0])
                    
