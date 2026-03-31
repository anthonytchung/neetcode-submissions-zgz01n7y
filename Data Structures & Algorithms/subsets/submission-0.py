class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Every possible combination


        """

        res = set()
        ans = []
        n = len(nums)
        def helper(i, subset):
            if i > n-1:
                return
            
            res.add(tuple(subset))
            helper(i + 1, subset[:])

            subset.append(nums[i])

            res.add(tuple(subset))
            helper(i+1, subset[:])

        helper(0, [])
        res.add(tuple([]))

        for item in res:
            ans.append(list(item))

        return ans