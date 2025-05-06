from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(c for row in grid for c in row if c != 0)
    stripe_color = max(cnt, key=cnt.get)
    stripe_rows = [r for r,row in enumerate(grid) if sum(1 for c in row if c==stripe_color) > w//2]
    stripe_cols = [c for c in range(w) if sum(1 for r in range(h) if grid[r][c]==stripe_color) > h//2]
    stripe_rows.sort()
    stripe_cols.sort()
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == 0 or v == stripe_color: continue
            d_r, sy = min((abs(r - y), y) for y in stripe_rows)
            d_c, sx = min((abs(c - x), x) for x in stripe_cols)
            if d_c <= d_r:
                nc = 2*sx - c
                if 0 <= nc < w and out[r][nc] == 0:
                    out[r][nc] = v
            else:
                if d_r % 2 == 0:
                    nr = 2*sy - r
                    if 0 <= nr < h and out[nr][c] == 0:
                        out[nr][c] = v
    return out