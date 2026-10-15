class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r=1,len(nums)-1
        while l<r:
            mid=(l+r)//2
            lessorequal=sum(1 for num in nums if num<=mid)
            if lessorequal<=mid:
                l=mid+1
            else:
                r=mid
        return l
