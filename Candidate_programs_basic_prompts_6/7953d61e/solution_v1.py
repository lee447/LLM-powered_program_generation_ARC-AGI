from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n=len(grid)
    m=2*n
    out=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i<n and j<n:
                out[i][j]=grid[i][j]
            elif i<n and j>=n:
                out[i][j]=grid[j-n][n-1-i]
            elif i>=n and j<n:
                out[i][j]=grid[2*n-1-i][n-1-j]
            else:
                out[i][j]=grid[2*n-1-j][i-n]
    return out