from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R=len(grid)
    C=len(grid[0])
    out=[[0]*(2*C) for _ in range(2*R)]
    for i in range(2*R):
        for j in range(2*C):
            if i<R:
                if j<C:
                    out[i][j]=grid[R-1-i][C-1-j]
                else:
                    out[i][j]=grid[R-1-i][j-C]
            else:
                if j<C:
                    out[i][j]=grid[i-R][C-1-j]
                else:
                    out[i][j]=grid[i-R][j-C]
    return out