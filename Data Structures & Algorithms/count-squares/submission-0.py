class CountSquares:

    def __init__(self):
        # a hashmap to store how many times each point appears
        self.ptsCount=defaultdict(int)
        # a list of all added points including duplicates
        self.pts=[]

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)]+=1
        self.pts.append(point)
        
    def count(self, point: List[int]) -> int:
        res=0
        px,py=point #query point
        for x, y in self.pts: #check if it can be the diagonal opp corner
            if (abs(py-y)!=abs(px-x)) or x==px or y==py:
                continue
            res+=self.ptsCount[(x,py)]*self.ptsCount[(px,y)]
        return res
        
