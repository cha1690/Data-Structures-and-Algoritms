class TrieNode:
    def __init__(self):
        self.children =  collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root= TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            curr= curr.children[letter]
        curr.is_word= True

    def search(self, word):
        curr = self.root
        for letter in word:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return curr.is_word

    def prefix(self, prefix):
        curr = self.root
        for letter in prefix:
            curr = curr.children.get(letter)
            if curr is None:
                return False
        return True