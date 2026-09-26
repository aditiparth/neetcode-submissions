class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumsquare(n)
            if n==1:
                return True
        return False
    def sumsquare(self,n:int)-> int:
        res=0
        for i in str(n):
            res+=int(i)*int(i)
        return res