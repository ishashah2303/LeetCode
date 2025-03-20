class Solution:
    def minimumCost(self, n, edges, queries):
        self.parent = [-1] * n
        self.depth = [0] * n

        component_cost = [-1] * n

        for edge in edges:
            self._union(edge[0], edge[1])

        for edge in edges:
            root = self._find(edge[0])
            component_cost[root] &= edge[2]

        answer = []
        for query in queries:
            start, end = query

            if self._find(start) != self._find(end):
                answer.append(-1)
            else:
                root = self._find(start)
                answer.append(component_cost[root])

        return answer

    def _find(self, node):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        if root1 == root2:
            return

        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1


'''
Time Complexity: O(NLogN)
Space Complexity: O(N)

Question:
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]s
'''