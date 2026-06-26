from heapq import heappush ,heappop

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def find_indegree(graph):
            indegree_graph = {t : 0 for t in graph}
            for node in graph:
                for neighbour in graph[node]:
                    indegree_graph[neighbour] += 1
            return indegree_graph
        
        def topo_sort(graph):
            pq :list[str] = []
            res :list[str] = []
            indegree_gph = find_indegree(graph)
            # Seed the heap/q with element having 0 indegree to start with
            for node in graph:
                if indegree_gph[node] == 0:
                    heappush(pq, node)
            while pq:
                root = heappop(pq)
                res.append(root)
                for neighbour in graph[root]:
                    indegree_gph[neighbour] -=1
                    if indegree_gph[neighbour] == 0:
                        heappush(pq, neighbour)
            return res if len(res) == len(graph) else None
        
        # INITIALIZE GRAPH
        # MAKE A GRAPH DICTIONARY WITH ALL POSSIBLE CHARACTER FROM WORDS
        graph: dict[str,list[str]] = {}
        for word in words:
            for w in word:
                if w not in graph:
                    graph[w] = []

        # Compare prev and curr words and build lineage
        # Any point we find mismatch and if not already present in graph, append to graph
        # Check edge case if prev and cur start with similar word sequence and if prev is > curr
        prev = words[0]
        for i in range(1, len(words)):
            curr = words[i]
            j = 0
            while j < len(prev) and j < len(curr):
                if prev[j] != curr[j]:
                    if curr[j] not in graph[prev[j]]:
                        graph[prev[j]].append(curr[j])
                    break
                j+=1
            if prev.startswith(curr) and len(prev) > len(curr):
                return ""
            prev = curr
        #graph: {'w': ['e'], 'r': ['t'], 't': ['f'], 'f': [], 'e': ['r']}
        s = topo_sort(graph)
        if s is None:
            return ""
        return "".join(s)