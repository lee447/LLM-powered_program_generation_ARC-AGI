from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    sr = sc = None
    for r in range(H - 1):
        for c in range(W - 1):
            a, b = grid[r][c], grid[r+1][c+1]
            if a == 8 and b == 1:
                sr, sc = r, c - 1
                break
            if a == 1 and b == 8:
                sr, sc = r, c
                break
        if sr is not None:
            break
    if sr is not None:
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if 0 <= i < H and 0 <= j < W and out[i][j] == 0:
                    out[i][j] = 4
    return out