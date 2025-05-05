from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    nonrows = [r for r in range(H) if any(grid[r][c] != 0 for c in range(W))]
    if not nonrows:
        return grid
    top, bot = nonrows[0], nonrows[-1]
    n = len(nonrows)
    odd = (n % 2 == 1)
    start = top + (1 if odd else 0)
    out = [[0]*W for _ in range(H)]
    for r in nonrows:
        row = grid[r]
        if (odd and (r == top or r == bot)) or (not odd and r == bot):
            out[r] = row.copy()
        else:
            k = r - start
            if k >= 0 and r != bot and k % 2 == 0:
                d = -1 if k % 4 == 0 else 1
                for c, v in enumerate(row):
                    if v:
                        nc = c + d
                        if 0 <= nc < W:
                            out[r][nc] = v
            else:
                out[r] = row.copy()
    return out