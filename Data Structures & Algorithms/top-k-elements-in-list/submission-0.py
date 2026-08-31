class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_k_val = heapq.nlargest(k, freq, key = freq.get)
        return max_k_val