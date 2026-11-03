import heapq


def prim(graph, start):
  mst = []
  visited = set([start])
  edges = [
      (weight, start, neighbor) for neighbor, weight in graph[start].items()
  ]
  heapq.heapify(edges)

  while edges:
    weight, u, v = heapq.heappop(edges)
    if v not in visited:
      visited.add(v)
      mst.append((u, v, weight))
      for neighbor, w in graph[v].items():
        if neighbor not in visited:
          heapq.heappush(edges, (w, v, neighbor))

  return mst


graph = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "C": 1, "D": 1, "E": 4},
    "C": {"A": 3, "B": 1, "F": 5},
    "D": {"B": 1, "E": 1},
    "E": {"B": 4, "D": 1},
    "F": {"C": 5},
}
print(f"Prim's MST edges: {prim(graph, 'A')}")