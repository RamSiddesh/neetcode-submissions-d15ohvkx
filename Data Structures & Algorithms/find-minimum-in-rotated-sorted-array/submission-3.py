class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l]<nums[r]:
                return min(res,nums[l])
                break
            res = min(res,nums[(l+r)//2])
            if nums[(l+r)//2]>=nums[l]:
                l = ((l+r)//2)+1
            else:
                r = ((l+r)//2)-1
        return res