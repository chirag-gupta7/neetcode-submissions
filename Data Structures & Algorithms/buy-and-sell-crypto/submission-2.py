class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        low = prices[0]

        for i in prices:
            if i < low:
                low = i
            elif i - low > max_num:
                max_num = i - low
        return max_num