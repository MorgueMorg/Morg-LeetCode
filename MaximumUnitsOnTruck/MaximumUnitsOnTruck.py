class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: x[1], reverse=True)
        i=0
        unit_count=0
        while i < len(boxTypes) and truckSize > 0 :
            unit_count += min(boxTypes[i][0],truckSize)*boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        return unit_count
       