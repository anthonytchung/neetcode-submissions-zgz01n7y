class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        index = -1

        while l <= r:
            half = l + ((r - l) // 2)

            if nums[half] == target:
                return half
            
            if nums[l] <= nums[half]:
                if target > nums[half] or target < nums[l]:
                    l = half + 1
                else:
                    r = half - 1
            else:
                if target > nums[r] or target < nums[half]:
                    r = half - 1
                else:
                    l = half + 1
    
            

        
        return index