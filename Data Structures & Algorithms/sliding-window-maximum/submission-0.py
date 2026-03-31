class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        output = []
        while r <= len(nums):
            maximum = max(nums[l:r])
            output.append(maximum)
            l += 1
            r += 1

        return output
