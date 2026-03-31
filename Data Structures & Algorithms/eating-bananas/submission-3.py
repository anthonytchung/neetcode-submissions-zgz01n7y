class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        piles: n piles of bananas
        piles[i] = number of bananas in a pile

        h = number of hours you HAVE to eat

        Cannot eat more than one pile an hour

        return minimum rate of eating bananas

        """

        

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r - l) // 2)
            time = 0 

            # print(piles, k)
            for pile in piles:
                time += math.ceil(pile / k)
            
            print(piles, k, time)
            if time <= h:
                res = min(res, k)
                r = k - 1
            elif time > h:
                l = k + 1

        return res
        



