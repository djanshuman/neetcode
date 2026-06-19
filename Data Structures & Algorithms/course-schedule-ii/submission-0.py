class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Generate Indegree Graph
        def get_indegree_graph(graph):
            indegree_graph = {t : 0 for t in graph}
            for node in graph:
                for neighbour in graph[node]:
                    indegree_graph[neighbour] +=1
            return indegree_graph


        def topo_sort(graph):
            q = deque()
            res = []
            indegree_gph = get_indegree_graph(graph)
            for node in graph:
                if indegree_gph[node] == 0:
                    q.append(node)
            while q:
                root = q.popleft()
                res.append(root)
                for neighbour in graph[root]:
                    indegree_gph[neighbour] -= 1
                    if indegree_gph[neighbour] == 0:
                        q.append(neighbour)
            return res if len(res) == len(graph) else None

        graph = {t : [] for t in range(numCourses)}
        

        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            
        return topo_sort(graph) or []