from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    centers = []
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] == 7:
                s = c
                while c < W and grid[r][c] == 7:
                    c += 1
                e = c - 1
                centers.append((r, (s + e) // 2))
            else:
                c += 1
    out = [[0] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                out[r][c] = 8
    for r, c in centers:
        out[r][c] = 6
        if r - 1 >= 0 and grid[r-1][c] != 0:
            out[r-1][c] = 6
        if r + 1 < H and grid[r+1][c] != 0:
            out[r+1][c] = 6
    return out