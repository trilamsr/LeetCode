class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        search_dict = set(words)
        mem = {}
        return [word for word in words if self.is_concated(word, search_dict, mem)]
    
    def is_concated(self, word, search, mem):
        if word in mem:
            return mem[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in search and (suffix in search or self.is_concated(suffix, search, mem)):
                mem[word] = True
                return True
        mem[word] = False
        return False