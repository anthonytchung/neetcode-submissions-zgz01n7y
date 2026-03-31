class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp[1]:
                result[stack[-1][0]] = temp[0] - stack[-1][0]
                stack.pop()
            stack.append(temp)
        return result