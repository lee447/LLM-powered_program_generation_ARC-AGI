from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    out = [row[:] for row in grid]
    points = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v != 0]
    if not points:
        return out
    rs, cs = zip(*points)
    min_r, max_r, min_c, max_c = min(rs), max(rs), min(cs), max(cs)
    h, w = max_r - min_r, max_c - min_c
    if h > w:
        mid = round((min_r + max_r) / 2)
        for c in range(len(out[0])):
            out[mid][c] = 3
    else:
        mid = round((min_c + max_c) / 2)
        for r in range(len(out)):
            out[r][mid] = 3
    return out