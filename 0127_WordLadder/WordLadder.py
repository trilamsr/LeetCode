



from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, words = deque([(beginWord, 1)]), set(wordList)
        if endWord not in words: return 0
        while queue:
            cur_word, distance = queue.popleft()
            if cur_word == endWord: return distance
            for neighbor in self.valid_adjacent(cur_word, words):
                queue.append((neighbor, distance+1))
                words.remove(neighbor)
        return 0
    
    def valid_adjacent(self, cur_word, words):
        cur = list(cur_word)
        for i, v in enumerate(cur):
            for char in string.ascii_lowercase:
                cur[i] = char
                neighbor = ''.join(cur)
                if neighbor in words:
                    yield neighbor
            cur[i] = v






from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        parents = self.get_parents(beginWord, endWord, wordList)
        ret = self.count_parents(parents, beginWord, endWord)
        return ret
    
    def count_parents(self, parents, beginWord, endWord):
        if endWord not in parents: return 0
        ret = 0
        while endWord != beginWord:
            ret += 1
            endWord = parents[endWord]
        return ret + 1

    def get_parents(self, beginWord, endWord, wordList):
        parent = {}
        words = set(wordList)
        if endWord not in words: return parent
        q1, q2 = deque([beginWord]), deque([endWord])
        a1, a2 = set([beginWord]), set([endWord])
        while q1 and q1:
            if len(q1) > len(q1):
                q1, q2 = q2, q1
                a1, a2 = a2, a1
            for _ in range(len(q1)):
                cur = q1.popleft()
                for nei in self.valid_adjacent(cur, words):
                    parent[nei] = cur
                    if nei in a2: return parent
                    q1.append(nei)
                    a1.add(nei)
                    words.remove(nei)
        return parent
    
    def valid_adjacent(self, cur, words):
        cur_list = list(cur)
        for i, v in enumerate(cur_list):
            for char in string.ascii_lowercase:
                cur_list[i] = char
                cur_word = ''.join(cur_list)
                if cur_word in words:
                    yield cur_word
            cur_list[i] = v