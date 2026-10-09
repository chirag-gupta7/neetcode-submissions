class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num , 0) + 1
        
        res = []
        for num, count in counts.items():
            if count > len(nums) // 3:
                res.append(num)
        return res