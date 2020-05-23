class Item:
    def __init__(self, log):
        self.id, self.rest = log.split(" ", 1)
        self.is_word = self.rest[0].isalpha()
        self.key = (1,) if not self.is_word else (0, self.rest, self.id)
        self.log = log
        
    def __lt__(self, other):
        return self.key < other.key

    def __str__(self):
        return self.log

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        items = [Item(item) for item in logs]
        items.sort()
        ret = [str(item) for item in items]
        return ret