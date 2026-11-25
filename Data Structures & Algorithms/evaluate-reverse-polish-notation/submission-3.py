class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                if token == "+":
                    value1 = stack.pop()
                    value2 = stack.pop()
                    stack.append(int(value2) + int(value1))
                elif token == "-":
                    value1 = stack.pop()
                    value2 = stack.pop()
                    stack.append(int(value2) - int(value1))
                elif token == "*":
                    value1 = stack.pop()
                    value2 = stack.pop()
                    stack.append(int(value2) * int(value1))
                elif token == "/":
                    value1 = stack.pop()
                    value2 = stack.pop()
                    stack.append(int(value2) / int(value1))

        return int(stack[0])