class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        maxa = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            maxa = max(maxa, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxa