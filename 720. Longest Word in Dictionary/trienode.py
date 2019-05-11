class TrieNode:
    def __init__(self, data):
        self.data = data
        self.isEnding = False
        self.children = [None] * 26

