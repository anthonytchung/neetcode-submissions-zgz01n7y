class Solution:
    def maxArea(self, heights: List[int]) -> int:
        peak = 0
        left, right = 0, len(heights) - 1
        while left < right:
            containerHeight = min(heights[left], heights[right])
            containerDistance = right - left
            area = containerHeight * containerDistance
            peak = max(area, peak)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return peak