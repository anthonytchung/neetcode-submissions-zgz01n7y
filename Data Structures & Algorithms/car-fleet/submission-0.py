class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carStack = []
        timeTaken = []

        for pos in reversed(sorted(position)):
            i = position.index(pos)
            timeTaken.append((pos, (target - position[i])/speed[i]))
        for time in timeTaken:
            if carStack:
                print(carStack[-1])
                if (carStack[-1][1] < time[1]):
                    carStack.append(time)
            else:
                carStack.append(time)
                



        return len(carStack)