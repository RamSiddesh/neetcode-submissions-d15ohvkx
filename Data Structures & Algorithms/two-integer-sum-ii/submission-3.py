class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ans_list = []
        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if numbers[i]==numbers[j]:
                    continue
                if numbers[i]+numbers[j] == target:
                    ans_list+=[i+1]
                    ans_list+=[j+1]
        return ans_list   


