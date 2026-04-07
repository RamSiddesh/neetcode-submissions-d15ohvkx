class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        out = []

        for i in strs:
            sorted_i = tuple(sorted(i))
            dict1[sorted_i].append(i)
        
        for i in dict1.values():
            out.append(i)

        return out


                