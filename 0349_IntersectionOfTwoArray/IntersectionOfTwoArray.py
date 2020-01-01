class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(); nums2.sort()
        if len(nums2) < len(nums1): nums1, nums2 = nums2, nums1
        p1, p2, ret = 0, 0, []
        while p1 < len(nums1):
            cur = nums1[p1]
            while p1 < len(nums1) and nums1[p1] <= cur: p1 += 1
            while p2 < len(nums2) and nums2[p2] < cur: p2 += 1
            if p2 < len(nums2) and cur == nums2[p2]: ret.append(cur)
        return ret