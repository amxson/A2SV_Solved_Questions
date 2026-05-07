from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        x = defaultdict(list)
        for i in edges:
            x[i[0]].append(i[1])
            x[i[1]].append(i[0])
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for i in x[node]:
                if i in visited:
                    continue
                if dfs(i):
                    return True
            return False
        return(dfs(source))


        