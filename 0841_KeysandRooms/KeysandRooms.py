class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        explored = set([0])
        queue = collections.deque([0])
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key in explored: continue
                queue.append(key)
                explored.add(key)
        return True if len(explored) == len(rooms) else False