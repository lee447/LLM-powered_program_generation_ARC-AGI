from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid[0])
    anchor = next(j for j,v in enumerate(grid[0]) if v==2)
    out = [[0]*N for _ in range(N)]
    mid = N//2
    for i in range(N):
        if i<=mid:
            off, c = i, 2
        else:
            off, c = N-1-i, 1
        l, r = anchor-off, anchor+off
        out[i][l] = c
        out[i][r] = c
    return out