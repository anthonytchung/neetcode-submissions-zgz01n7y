class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        peak = count
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] - nums[i] == 1:
                count += 1
                if count > peak:
                    peak = count
            else:
                count = 1
        

        return peak