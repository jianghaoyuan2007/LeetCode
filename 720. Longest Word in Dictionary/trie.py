from trienode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode("/")

    def insert(self, text):
        p = self.root
        for i in range(len(text)):
            index = ord(text[i]) - ord("a")
            if not p.children[index]:
                p.children[index] = TrieNode(text[i])
            p = p.children[index]
        p.isEnding = True

    def find(self, pattern):
        p = self.root
        for i in range(len(pattern)):
            index = ord(pattern[i]) - ord("a")
            if not p.children[index]:
                return False
            p = p.children[index]
        return p.isEnding

