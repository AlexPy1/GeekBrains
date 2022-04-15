# 1319. Number of Operations to Make Network Connected

class Solution:
    def makeConnected(self, n: int, connections) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        groups = [n]

        def find(x: int) -> int:
            p = parent[x]

            while p != parent[p]:
                p = parent[p]

            parent[x] = p

            return p

        def union(x: int, y: int) -> None:
            x, y = find(x), find(y)

            if x != y:
                if rank[y] > rank[x]:
                    x, y = y, x

                parent[y] = x
                rank[x] += rank[y]
                groups[0] -= 1

        for node, neigh in connections:
            union(node, neigh)

        if len(connections) >= n - 1:
            return groups[0] - 1
        return -1