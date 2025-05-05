from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_rows = [i for i in range(h) if len(set(grid[i])) == 1 and grid[i][0] != 0]
    stripe_rows.sort()
    out = [row[:] for row in grid]
    for idx, sr in enumerate(stripe_rows):
        stripe_color = grid[sr][0]
        above_start = 0 if idx == 0 else stripe_rows[idx - 1] + 1
        above_end = sr
        below_start = sr + 1
        below_end = stripe_rows[idx + 1] if idx + 1 < len(stripe_rows) else h
        height_above = above_end - above_start
        height_below = below_end - below_start
        if height_below < height_above:
            continue
        offset = below_start - above_start
        for r in range(above_start, above_end):
            tr = r + offset
            for c in range(w):
                v = grid[r][c]
                if v != 0 and v < stripe_color:
                    out[tr][c] = v
    return out