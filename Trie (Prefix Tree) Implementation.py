# Trie (Prefix Tree) Implementation
class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_end_of_word = False


class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for ch in word:
      if ch not in curr.children:
        curr.children[ch] = TrieNode()
      curr = curr.children[ch]
    curr.is_end_of_word = True

  def search(self, word):
    curr = self.root
    for ch in word:
      if ch not in curr.children:
        return False
      curr = curr.children[ch]
    return curr.is_end_of_word

  def starts_with(self, prefix):
    curr = self.root
    for ch in prefix:
      if ch not in curr.children:
        return False
      curr = curr.children[ch]
    return True


trie = Trie()
trie.insert("apple")
print(f"Search 'apple': {trie.search('apple')}")
print(f"Search 'app': {trie.search('app')}")
print(f"Starts with 'app': {trie.starts_with('app')}")