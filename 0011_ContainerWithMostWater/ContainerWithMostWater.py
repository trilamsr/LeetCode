class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret, lo, hi = 0, 0, len(height)-1
        while lo < hi:
            cur_area = (hi-lo)*min(height[lo], height[hi])
            ret = max(cur_area, ret)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return ret


# O(N^2), O(1) space - Time limit exceed
class Solution:
    @staticmethod
    def get_area(width, height):
        return width*height
    
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                cur_area = Solution.get_area(j-i ,min(height[i], height[j]))
                ret = max(ret, cur_area)
        return ret