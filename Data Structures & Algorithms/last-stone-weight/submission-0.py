class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)

            newStone = abs(stone1 - stone2)
            if newStone == 0:
                continue
            else:
                heapq.heappush_max(stones, newStone)
        
        return stones[0] if len(stones) > 0 else 0