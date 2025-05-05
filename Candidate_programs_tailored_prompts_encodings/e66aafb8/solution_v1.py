from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    min_r, min_c = H, W
    max_r = max_c = -1
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 0:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    mask_h = max_r - min_r + 1
    mask_w = max_c - min_c + 1
    result = [[0] * mask_w for _ in range(mask_h)]
    if mask_h >= mask_w:
        for i in range(mask_h):
            r = min_r + i
            mr = H - 1 - r
            for j in range(mask_w):
                c = min_c + j
                result[i][j] = grid[mr][c]
    else:
        for i in range(mask_h):
            r = min_r + i
            for j in range(mask_w):
                c = min_c + j
                mc = W - 1 - c
                result[i][j] = grid[r][mc]
    return result