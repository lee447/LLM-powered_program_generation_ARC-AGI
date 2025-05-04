from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    min_r = min(r for r, _ in pts)
    max_r = max(r for r, _ in pts)
    min_c = min(c for _, c in pts)
    max_c = max(c for _, c in pts)
    tile = [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]
    th, tw = len(tile), len(tile[0])
    N = max(H + th + 1, W + tw + 1)
    if N % 2 == 0:
        N += 1
    res = [[0]*N for _ in range(N)]
    mid = N // 2
    dr0 = min_r - H//2
    dc0 = min_c - W//2
    for i in range(th):
        for j in range(tw):
            if tile[i][j] != 4:
                continue
            for sr in (-1, 1):
                for sc in (-1, 1):
                    r = mid + sr*(dr0 + i)
                    c = mid + sc*(dc0 + j)
                    if 0 <= r < N and 0 <= c < N:
                        res[r][c] = 4
    return res