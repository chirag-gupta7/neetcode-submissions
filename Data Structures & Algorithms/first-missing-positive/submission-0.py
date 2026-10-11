class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numss = set(nums)
        j = 1
        while True:
            if j not in numss:
                return j
            j += 1
            