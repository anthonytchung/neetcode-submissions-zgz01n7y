class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
        output = 0
        stack = []

        for num in tokens:
            try:
                stack.append(int(num))
                print(stack)
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(op[num](num1,num2)))
            

        return stack[0]