class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parathesises = []
        def dfs(numOpen, numClose, parathesis):
            if numOpen < numClose:
                return
            if numOpen == n and numClose == n:
                parathesises.append(parathesis)
                return
            
            if numOpen < n:
                newParathesis = parathesis + "("
                dfs(numOpen + 1, numClose, newParathesis)
            if numClose < n:
                newParathesis = parathesis + ")"
                dfs(numOpen, numClose + 1, newParathesis)
            

        dfs(1, 0, "(")
        return parathesises
            