class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_word = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        frequency = collections.Counter(words)
        max_key = lambda key: frequency[key] if key not in banned else 0 
        return max(frequency, key=max_key)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_word = set(banned)
        counter = collections.Counter()
        for word in self.iterable(paragraph):
            if word not in banned_word: counter[word] += 1
        return max(counter, key=lambda x: counter[x])

    def iterable(self, s):
        lo, hi = 0, 0
        while lo < len(s):
            if not s[lo].isalpha():
                lo += 1
                hi = lo
                continue
            while hi < len(s) and s[hi].isalpha():
                hi += 1
            yield s[lo:hi].lower()
            lo = hi
            
        