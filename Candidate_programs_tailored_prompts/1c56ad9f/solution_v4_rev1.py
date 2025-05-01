from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for color in set(v for row in grid for v in row if v):
        rows = {r: [c for c in range(w) if grid[r][c] == color] for r in range(h)}
        rows = {r: cols for r, cols in rows.items() if cols}
        max_count = max(len(cols) for cols in rows.values())
        stripe_rows = sorted(r for r, cols in rows.items() if len(cols) == max_count)
        for seg in range(len(stripe_rows) - 1):
            start, end = stripe_rows[seg], stripe_rows[seg + 1]
            sign = -1 if seg % 2 == 0 else 1
            for j, r in enumerate(range(start + 1, end)):
                delta = sign * [-1, 0, 1, 0][j % 4]
                for c in rows[r]:
                    nc = c + delta
                    if 0 <= nc < w:
                        out[r][c] = 0
                        out[r][nc] = color
    return out