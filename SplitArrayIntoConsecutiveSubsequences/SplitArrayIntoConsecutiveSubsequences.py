# ! Алгоритм Кучи

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        heap=[]
        
        for x in nums:
            
            while heap and (x>(heap[0][0]+1)):
                length= heapq.heappop(heap)
                if length[1]<3:
                    return False
            
            if heap and x==(heap[0][0]+1):
                length=heapq.heappop(heap)
                heapq.heappush(heap,(x,length[1]+1))
            else:
                heapq.heappush(heap,(x,1))
        
        while heap:
            if heapq.heappop(heap)[1]<3:
                return False
        
        return True