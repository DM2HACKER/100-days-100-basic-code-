# Bellman-Ford Algorithm
def bellman_ford(vertices, edges, start):
  dist = {v: float("inf") for v in vertices}
  dist[start] = 0

  for _ in range(len(vertices) - 1):
    for u, v, w in edges:
      if dist[u] != float("inf") and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w

  # Check for negative weight cycles
  for u, v, w in edges:
    if dist[u] != float("inf") and dist[u] + w < dist[v]:
      print("Graph contains a negative weight cycle!")
      return None

  return dist


vertices = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B", -1),
    ("A", "C", 4),
    ("B", "C", 3),
    ("B", "D", 2),
    ("B", "E", 2),
    ("D", "B", 1),
    ("D", "C", 5),
    ("E", "D", -3),
]
print(f"Bellman-Ford distances from A: {bellman_ford(vertices, edges, 'A')}")