class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''res=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append((t,i))
        return res'''
        res=[]
        for i in range(len(temperatures)):
            count=1
            j=i+1
            while j<len(temperatures):
                if temperatures[j]>temperatures[i]:
                    break
                j+=1
                count+=1
            count=0 if j==len(temperatures) else count
            res.append(count)
        return res
            