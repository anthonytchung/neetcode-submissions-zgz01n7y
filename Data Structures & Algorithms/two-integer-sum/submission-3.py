class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addition = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in addition and addition[complement] != i:
                return sorted([i, addition.get(complement)])
                
            addition[nums[i]] = i
            
        return None