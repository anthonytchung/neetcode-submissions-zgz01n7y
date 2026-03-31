class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        if len(s) < len(t):
            return output
        if s == t:
            return t
        
        l, r = 0, 0
        minLen = float('inf')
        tCount = Counter(t)
        windowCount = Counter()
        have = 0
        need = len(t)

        while r < len(s):
            char = s[r]
            windowCount[char] += 1
            if char in tCount and windowCount[char] == tCount[char]:
                have += 1
            
            while have == need:
                char = s[l]
                if r - l < minLen:
                    output = s[l:r+1]
                    minLen = r - l
                

                windowCount[char] -= 1

                if char in tCount and windowCount[char] < tCount[char]:
                    have -= 1
                l += 1

            r += 1

        

        return output
        
        