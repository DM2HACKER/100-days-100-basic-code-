# Find Minimum Element in a BST
class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_min_bst(root):
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr.val if curr else None


root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)

print(f"Minimum value in BST: {find_min_bst(root)}")

# Graph Representation Using Adjacency List
class Graph:

  def __init__(self):
    self.adj_list = {}

  def add_edge(self, u, v):
    if u not in self.adj_list:
      self.adj_list[u] = []
    if v not in self.adj_list:
      self.adj_list[v] = []
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)  # For undirected graph


g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
print(f"Adjacency List: {g.adj_list}")

# Breadth-First Search (BFS) for Graphs
from collections import deque


def bfs(graph, start):
  visited = set()
  queue = deque([start])
  visited.add(start)
  result = []

  while queue:
    node = queue.popleft()
    result.append(node)
    for neighbor in graph.get(node, []):
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  return result


graph = {1: [2, 3], 2: [1, 4, 5], 3: [1], 4: [2], 5: [2]}
print(f"BFS Traversal: {bfs(graph, 1)}")