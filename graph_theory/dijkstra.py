import heapq


def dijkstra(st: int, adj: list, d: list) -> list:
    pq = []
    heapq.heappush(pq, (0, st))
    d[st] = 0

    while pq:
        dst, u = heapq.heappop(pq)
        if (d[u] < dst):
            continue
        for v, w in adj[u]:
            cost = d[u] + w
            if (cost < d[v]):
                d[v] = cost
                heapq.heappush(pq, (cost, v))
    
    return d
