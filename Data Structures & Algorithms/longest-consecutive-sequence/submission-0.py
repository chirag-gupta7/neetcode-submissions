class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        counter = 0
        for i in s:                 # <-- iterate over set, not nums
            if i - 1 not in s:
                l = 1
                while i + l in s:
                    l += 1
                counter = max(counter, l)
        return counter