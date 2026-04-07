class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        sorted_keys = sorted(dict1, key=dict1.get, reverse=True)

        return sorted_keys[:k]
