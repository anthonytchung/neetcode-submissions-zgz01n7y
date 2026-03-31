class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {}
        frequency = [[] for i in range(len(nums) + 1)]
        listNum = []
        for num in nums:
            found[num] = 1 + found.get(num, 0)
        for key, value in found.items():
            frequency[value].append(key)

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                listNum.append(num)
                if len(listNum) == k:
                    return listNum
        return listNum