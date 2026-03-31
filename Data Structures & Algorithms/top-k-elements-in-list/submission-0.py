class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            found[num] = found.get(num,0) + 1
        for key, value in found.items():
            freq[value].append(key)
        listNum = []
        
        for i in range(len(freq)-1, 0, -1):
            print(freq[i])
            for num in freq[i]:
                listNum.append(num)
                if len(listNum) == k:
                    return listNum

            
        return listNum
