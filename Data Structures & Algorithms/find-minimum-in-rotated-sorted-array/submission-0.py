class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums)-1

        
        
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])

            half = l + int((r-l) / 2)
            minimum = min(minimum, nums[half])

            if nums[half] >= nums[l]:
                l = half+1
            else:
                r = half-1
        
        return minimum
