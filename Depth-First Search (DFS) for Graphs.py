# Depth-First Search (DFS) for Graphs
def dfs(graph, start, visited=None, result=None):
  if visited is None:
    visited = set()
  if result is None:
    result = []

  visited.add(start)
  result.append(start)

  for neighbor in graph.get(start, []):
    if neighbor not in visited:
      dfs(graph, neighbor, visited, result)
  return result


graph = {1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}
print(f"DFS Traversal: {dfs(graph, 1)}")


