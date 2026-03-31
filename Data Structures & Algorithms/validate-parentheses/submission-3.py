class Solution:
    def isValid(self, s: str) -> bool:
        contains = {")" : "(", "}" : "{", "]" : "[",}
        if len(s) < 2:
            return False
        stack = []
        for char in s:
            print(char)
            if char in contains:
                if not stack or stack[-1] != contains[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
            
            