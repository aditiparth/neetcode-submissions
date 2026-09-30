class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        self.perimeter=0
        visit=set()
        q=deque()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            visit.add((r,c))
            q.append([r,c])
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r<0 or r==rows or c<0 or c==cols):
                        self.perimeter+=1
                    elif grid[r][c]==0:
                        self.perimeter+=1
                    elif grid[r][c]==1 and (r,c) not in visit:
                        q.append([r,c])
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    bfs(r,c)
        return self.perimeter

