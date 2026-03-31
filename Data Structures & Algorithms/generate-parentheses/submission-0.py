class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        results = []

        def recursiveTrack(openVar, closeVar):
            if openVar == closeVar == n:
                results.append("".join(stack))
                return
            
            if openVar < n:
                stack.append("(")
                recursiveTrack(openVar + 1, closeVar)
                stack.pop()
                

            if closeVar < openVar:
                stack.append(")")
                recursiveTrack(openVar, closeVar + 1)
                stack.pop()

        recursiveTrack(0, 0)
        return results
        