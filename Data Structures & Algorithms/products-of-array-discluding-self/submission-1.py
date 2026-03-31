class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listNum = [0] * len(nums)
        total = 1
        countZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                total = total * nums[i]
            else:
                countZero += 1
        
        if countZero >= 2:
            return listNum
        elif countZero == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    listNum[i] = total
        else:
            for i in range(len(nums)):
                listNum[i] = int(total / nums[i])
            
            
        
        return listNum