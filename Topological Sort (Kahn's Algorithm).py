from collections import deque


def topological_sort(num_nodes, edges):
  adj = {i: [] for i in range(num_nodes)}
  in_degree = [0] * num_nodes

  for u, v in edges:
    adj[u].append(v)
    in_degree[v] += 1

  queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
  res = []

  while queue:
    node = queue.popleft()
    res.append(node)
    for neighbor in adj[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)

  return res if len(res) == num_nodes else []  # Returns empty if cycle exists


num_nodes = 6
edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
print(f"Topological Sort order: {topological_sort(num_nodes, edges)}")