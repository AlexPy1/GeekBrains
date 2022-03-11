# Replace Words

class TrieNode():

    def __init__(self):
        self.children = {}


class Trie():

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):

        curr = self.root

        for char in word:

            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

    def search(self, word, dictionary):

        curr = self.root

        res = ""

        for char in word:

            if char not in curr.children:
                break

            res += char

            if res in dictionary:
                break

            curr = curr.children[char]

        return res


class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        dictionary = set(dictionary)

        sentence = sentence.split()

        for i, word in enumerate(sentence):

            w = trie.search(word, dictionary)

            if w in dictionary:
                sentence[i] = w

        return " ".join(sentence)
