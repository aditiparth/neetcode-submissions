class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks) #hashmap to count freq
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap) #orders it
        time=0
        q=deque() #contains a pair of values [-cnt,idletime]
        while maxHeap or q:
            time+=1 
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap) #since we're using neg values
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time