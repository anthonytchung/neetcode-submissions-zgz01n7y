class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        count = 1
        peak = count
        for num in numSet:
            if num-1 not in numSet:
                while num+count in numSet:
                    count+= 1
            peak = max(peak, count)
            count = 1

        return peak
