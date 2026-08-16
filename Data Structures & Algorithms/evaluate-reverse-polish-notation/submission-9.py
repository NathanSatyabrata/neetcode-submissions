class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if stack and tokens[i] in operators:
                if tokens[i] == '+':
                    res = int(stack[-1] + stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i] == '-':
                    res = int(stack[-2] - stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i] == '*':
                    res = int(stack[-1] * stack[-2])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i] == '/':
                    res = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
            else:
                stack.append(int(tokens[i]))

        return stack[0]
            


