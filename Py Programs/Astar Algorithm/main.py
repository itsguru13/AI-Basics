import heapq

def a_star(start, goal, graph):
    heap = [(0, start)]
    v = set()
    p = {}
    g = {start: 0}
    while heap:
        n = heapq.heappop(heap)
        if n == goal:
            return n + [p[n] for n in p][::-1]
        if n in v:
            continue
        v.add(n)
        for i in graph.neighbors(n):
            cost = g[n] + graph.cost(n, i)
            if i not in g or cost < g[i]:
                g[i] = cost
                heapq.heappush(heap, (cost + heuristic_cost_estimate(i, goal), i))
                p[i] = n
    return None

def heuristic_cost_estimate(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


a_star(10, 20, 100)