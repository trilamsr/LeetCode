class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        for i in range(n):
            left[i] = height[i] if i == 0 else max(left[i-1], height[i])
            right[n-1-i] = height[n-1-i] if i == 0 else max(right[n-i], height[n-1-i])
        return sum([min(left[i], right[i])-height[i] for i in range(n)])