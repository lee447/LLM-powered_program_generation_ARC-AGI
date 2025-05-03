from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rmin = next(r for r in range(H) if any(grid[r][c] != 0 for c in range(W)))
    pattern = [0, -1, 0, 1]
    out = [[0]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                shift = pattern[(r - rmin) % 4]
                out[r][c + shift] = v
    return out