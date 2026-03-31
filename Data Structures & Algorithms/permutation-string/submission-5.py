class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        windowCount = Counter(s2[:len(s1)])
        if s1Count == windowCount:
            return True
        for i in range(len(s1), len(s2)):
            leftChar = s2[i-len(s1)]
            rightChar = s2[i]

            windowCount[leftChar] -= 1
            windowCount[rightChar] += 1

            if s1Count == windowCount:
                return True

        return False

            
