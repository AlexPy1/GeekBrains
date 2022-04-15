# 2000. Reverse Prefix of Word
# Решил без 2 указателей. Если ты это читаешь, значит я не придумал как решить с 2


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            ind = word.index(ch)
        else:
            return word
        res = ''
        for i in range(len(word)):
            if ind >= 0:
                res += word[ind]
                ind -= 1
            else:
                res += word[i]
        return res

