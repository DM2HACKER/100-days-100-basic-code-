import heapq


def dijkstra(graph, start):
  distances = {node: float("inf") for node in graph}
  distances[start] = 0
  pq = [(0, start)]  # (distance, node)

  while pq:
    current_dist, current_node = heapq.heappop(pq)

    if current_dist > distances[current_node]:
      continue

    for neighbor, weight in graph[current_node].items():
      distance = current_dist + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))

  return distances


# Graph representation: {node: {neighbor: weight}}
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2},
}
print(f"Shortest paths from A: {dijkstra(graph, 'A')}")