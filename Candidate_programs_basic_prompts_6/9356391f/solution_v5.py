from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    colors = [v for v in grid[0] if v != 0]
    sr = sc = None
    for i in range(2, H):
        for j in range(W):
            if grid[i][j] != 0:
                sr, sc = i, j
                break
        if sr is not None:
            break
    n = len(colors)
    for k in range(n - 1, -1, -1):
        c = colors[k]
        for x in range(sc - k, sc + k + 1):
            if 0 <= sr - k < H and 0 <= x < W:
                res[sr - k][x] = c
            if 0 <= sr + k < H and 0 <= x < W:
                res[sr + k][x] = c
        for y in range(sr - k, sr + k + 1):
            if 0 <= y < H and 0 <= sc - k < W:
                res[y][sc - k] = c
            if 0 <= y < H and 0 <= sc + k < W:
                res[y][sc + k] = c
    return res