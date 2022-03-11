# Design Add and Search Words Data Structure

class TrieNode():
    def __init__(self):
        self.children = {}


class WordDictionary:
    dictionary = []

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        curr = self.root
        res = ""

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            res += char
        WordDictionary.dictionary.append(res)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in WordDictionary.dictionary
        else:
            for elem in WordDictionary.dictionary:
                if len(elem) == len(word):
                    i = 0
                    while i < len(word):
                        if word[i] == '.':
                            i += 1
                            continue
                        if elem[i] != word[i]:
                            break
                        i += 1
                    if i == len(word):
                        return True
            return False