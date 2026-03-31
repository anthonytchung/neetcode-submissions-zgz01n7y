class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums: List[int], target) -> bool:
            l, r = 0, len(nums) - 1
            
            while l <= r:
                half = l + int((r-l) / 2)
                if target == nums[half]:
                    return True
                elif target > nums[half]:
                    l = half + 1
                elif target < nums[half]:
                    r = half - 1
        
            return False

        for list in matrix:
            if binarySearch(list, target):
                return True
        return False
    
    
            
