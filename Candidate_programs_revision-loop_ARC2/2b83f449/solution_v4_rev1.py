from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    centers = set()
    for r in range(H):
        c = 0
        while c < W:
            if grid[r][c] == 7:
                s = c
                while c < W and grid[r][c] == 7:
                    c += 1
                e = c - 1
                centers.add((s + e) // 2)
            else:
                c += 1
    out = [[0] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 0:
                out[r][c] = 0
            elif c in centers:
                out[r][c] = 6
            else:
                out[r][c] = 8
    return out