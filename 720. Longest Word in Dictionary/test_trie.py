from unittest import TestCase
from trie import Trie


class TestTrie(TestCase):
    def test_insert_and_find(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.find("apple"))
