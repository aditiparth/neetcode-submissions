class Solution:
    def hammingWeight(self, n: int) -> int:
        res=''
        while n>0:
            res=str(n&1)+res
            n>>=1
        count=0
        for i in res:
            if int(i)==1:
                count+=1
        return count