class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        pq, g = [(0,src,K+1)], collections.defaultdict(dict)
        for s,d,w in flights: 
            g[s][d] = w
        while pq:
            cost, s, k = heapq.heappop(pq)
            if s == dst: 
                return cost
            if not k: continue
            for d in g[s]:
                heapq.heappush(pq, (cost+g[s][d], d, k-1))
        return -1