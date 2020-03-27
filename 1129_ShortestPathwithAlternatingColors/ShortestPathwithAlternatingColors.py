class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = self.record_route(red_edges)
        blue = self.record_route(blue_edges)
        ret = [math.inf]*n
        self.bfs(ret, red, blue)
        self.bfs(ret, blue, red)
        for i, v in enumerate(ret):
            if v == math.inf: ret[i] = -1
        return ret
    
    def bfs(self,ret, red, blue):
        level = 0
        red_vis, blue_vis = set(), set()
        que = collections.deque([0])
        record, visited = red, red_vis
        while que:
            for _ in range(len(que)):
                origin = que.popleft()
                ret[origin] =  min(ret[origin], level)
                for des in record[origin]:
                    if des in visited: continue
                    que.append(des)
                    visited.add(des)
            level += 1
            record = red if record == blue else blue
            visited = red_vis if visited == blue_vis else blue_vis
        return ret
    
    def record_route(self, paths):
        record = collections.defaultdict(list)
        for ori, des in paths:
            record[ori].append(des)
        return record

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = self.record_route(red_edges)
        blue = self.record_route(blue_edges)
        ret = [math.inf]*n
        self.bfs(ret, copy.deepcopy(red), copy.deepcopy(blue), n)
        self.bfs(ret, copy.deepcopy(blue), copy.deepcopy(red), n)
        for i, v in enumerate(ret):
            if v == math.inf: ret[i] = -1
        return ret
    
    def bfs(self,ret, red, blue, n):
        level = 0
        que = collections.deque([0])
        record = red
        while que:
            for _ in range(len(que)):
                origin = que.popleft()
                ret[origin] =  min(ret[origin], level)
                while origin in record and record[origin]:
                    que.append(record[origin].pop())
            level += 1
            record = red if record == blue else blue
        return ret
        
    def record_route(self, paths):
        record = {}
        for ori, des in paths:
            if not ori in record: record[ori] = []
            record[ori].append(des)
        return record