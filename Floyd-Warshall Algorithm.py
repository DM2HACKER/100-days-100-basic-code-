def floyd_warshall(n, graph):
  INF = float("inf")
  dist = [[INF] * n for _ in range(n)]

  for i in range(n):
    dist[i][i] = 0

  for u in graph:
    for v, w in graph[u].items():
      dist[u][v] = w

  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  return dist


# Example graph with 4 nodes (0 to 3)
graph = {
    0: {1: 3, 2: 6},
    1: {2: 2, 3: 1},
    2: {3: 4},
    3: {},
}
print(f"All-pairs shortest paths matrix:\n{floyd_warshall(4, graph)}")