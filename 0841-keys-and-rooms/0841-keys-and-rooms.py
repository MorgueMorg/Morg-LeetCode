class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = {0}
        while stack:
            node = stack.pop()
            for k in rooms[node]:
                if k not in visited:
                    visited.add(k)
                    stack.append(k)
        return len(visited) == len(rooms)