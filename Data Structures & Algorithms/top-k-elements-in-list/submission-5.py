class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        out = []
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        while k!=0:
            max_key = max(dict1, key=dict1.get)
            del dict1[max_key]
            out.append(max_key)
            k-=1
        return out
