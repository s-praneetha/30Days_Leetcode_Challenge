class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        ans = []
        
        for scr, dep in tickets:
            graph[scr].append(dep)
        for key in graph:
            graph[key].sort()
        
        def dfs(node):
            arr = graph[node]
            while arr:
                dfs(arr.pop(0))
            ans.append(node)
        
        dfs("JFK")
        return ans[::-1]