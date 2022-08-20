class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])    
        fuel = startFuel
        cnt, prev = 0, 0
        miss = []
    
        for pos, gas in stations:
            dis, prev = pos - prev, pos  
            if fuel < dis: 
                while miss and fuel < dis: 
                    fuel += -heapq.heappop(miss)
                    cnt += 1 
                if fuel < dis:
                    return -1  
            fuel -= dis
            # Метод кучи
            heapq.heappush(miss, -gas)  
            
        return cnt