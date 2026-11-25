class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        for element in s:
            if element in ["(", "{", "["]:
                stack.append(element)
            else:
                if stack != [] and stack[-1] == "{" and element == "}":
                    stack.pop()
                elif stack != [] and stack[-1] == "(" and element == ")":
                    stack.pop()
                elif stack != [] and stack[-1] == "[" and element == "]":
                    stack.pop()
                else:
                    stack.append(element)
        return stack == []