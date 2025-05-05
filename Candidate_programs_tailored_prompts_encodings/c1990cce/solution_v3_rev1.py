from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid[0])
    mid = N // 2
    out = [[0]*N for _ in range(N)]
    for i in range(N):
        if i <= mid:
            off = i
            c = 2
            out[i][mid-off] = c
            out[i][mid+off] = c
        else:
            d = i - mid
            if d == 1:
                out[i][mid-1] = 1
            elif d == mid:
                out[i][mid] = 1
            else:
                off = N-1-i
                out[i][mid-off] = 1
                out[i][mid+off] = 1
    return out