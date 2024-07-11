class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        #  split function
        words = []
        word = ''
        delimitation = ' '
        for c in s:
            if c not in delimitation:
                word += c
            elif word:
                words.append(word)
                word = ''

        if word:
            words.append(word)
        
        # check the length
        if len(pattern) != len(words):
            return False
        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern,words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True