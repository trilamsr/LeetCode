from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ret = Counter(A[0])
        for i in A:
            ret &= Counter(i)
        return list(ret.elements())