class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin,curmax=1,1
        for n in nums:
            tmp=curmax*n
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(tmp,n*curmin,n) #since we updated curmax
            res=max(res,curmax)
        return res
