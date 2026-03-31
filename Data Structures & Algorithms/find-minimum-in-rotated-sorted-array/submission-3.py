class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums)-1

        
        
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])

            print(f"left:  {nums[l]}")
            print(f"right:  {nums[r]}")

            half = l + int((r-l) / 2)
            print(f"half:  {nums[half]}")
            minimum = min(minimum, nums[half])
            print(f"minimum:  {minimum}")

            if nums[half] >= nums[l]:
                l = half+1
            else:
                r = half-1
        
        return minimum
