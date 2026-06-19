class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Generate Indegree Graph
        def get_indegree(graph):
            indegree_gph = {node : 0 for node in graph}
            for node in graph:
                for neighbour in graph[node]:
                    indegree_gph[neighbour] += 1
            return indegree_gph
        
        # Perform Topo Sort 
        def topo_sort(graph):
            q = deque()
            res = []
            indegree_graph = get_indegree(graph)
            for node in graph:
                if indegree_graph[node] == 0:
                    q.append(node)
            while q:
                root = q.popleft()
                res.append(root)
                for neighbour in graph[root]:
                    indegree_graph[neighbour] -= 1
                    if indegree_graph[neighbour] == 0:
                        q.append(neighbour)
            return True if len(graph) == len(res) else False
     
        #Build Graph
        graph = {i: [] for i in range(numCourses)}
        for a ,b in prerequisites:
            graph[b].append(a)
        return topo_sort(graph)