class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        dp  = [[0]*(n) for _ in range(m)]
        ret = [[0]*(n) for _ in range(m)]
        inbound = lambda i, j: 0 <= i < m and 0 <= j < n
        val = lambda i, j, arr: arr[i][j] if inbound(i, j) else 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = val(i, j, mat)+val(i-1, j, dp)+val(i, j-1, dp)-val(i-1, j-1, dp)
        for i in range(m):
            for j in range(n):
                hi_row, hi_col = min(m-1, i+k), min(n-1, j+k)
                lo_row, lo_col = i-k-1, j-k-1
                total= val(hi_row, hi_col, dp)
                top= val(lo_row, hi_col, dp)
                left= val(hi_row, lo_col, dp)
                dual = val(lo_row, lo_col, dp)
                ret[i][j] = total - top - left + dual
        return ret