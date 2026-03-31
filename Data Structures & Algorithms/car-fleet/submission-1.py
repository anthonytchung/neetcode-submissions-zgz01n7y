class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carStack = []
        timeTaken = []

        for i in range(len(position)):
            timeTaken.append((position[i], (target - position[i])/speed[i]))
        
        timeTaken.sort(reverse=True)

        for time in timeTaken:
            carStack.append(time)
            if len(carStack) > 1:
                if carStack[-2][1] >= time[1]:
                    carStack.pop()
                



        return len(carStack)