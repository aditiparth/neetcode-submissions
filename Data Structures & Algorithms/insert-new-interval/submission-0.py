class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:#new intervals goes before
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:#not overlapping
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        res.append(newInterval) #if iteration is done, inserted at the end
        return res

        