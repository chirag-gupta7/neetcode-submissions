class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ss = set(nums)
        sss = Counter(ss)
        ssss = Counter(nums)
        if sss == ssss:
            return False
        return True