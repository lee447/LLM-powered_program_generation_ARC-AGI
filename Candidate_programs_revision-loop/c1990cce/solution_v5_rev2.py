from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    w = len(grid[0])
    c0 = grid[0].index(2)
    L = min(c0, w - 1 - c0)
    H = 2 * L + 1
    out = [[0] * w for _ in range(H)]
    for r in range(L + 1):
        out[r][c0 - r] = 2
        out[r][c0 + r] = 2
    for r in range(L, H):
        d = r - L
        if d % 2 == 0:
            for c in range(w):
                if out[r][c] == 0 and (r + c + c0) % 4 == 0:
                    out[r][c] = 1
        else:
            for c in range(w):
                if out[r][c] == 0 and (r - c + c0) % 4 == 0:
                    out[r][c] = 1
    return out