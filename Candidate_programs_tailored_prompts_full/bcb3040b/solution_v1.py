from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    reds = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    segs = []
    if len(reds) == 2:
        segs = [tuple(reds)]
    else:
        for i in range(len(reds)):
            for j in range(i + 1, len(reds)):
                r1, c1 = reds[i]
                r2, c2 = reds[j]
                if r1 == r2 or c1 == c2:
                    segs.append(((r1, c1), (r2, c2)))
    out = [row[:] for row in grid]
    for (r1, c1), (r2, c2) in segs:
        if r1 == r2:
            y = r1
            x0, x1 = sorted([c1, c2])
            coords = [(y, x) for x in range(x0, x1 + 1)]
        elif c1 == c2:
            x = c1
            y0, y1 = sorted([r1, r2])
            coords = [(y, x) for y in range(y0, y1 + 1)]
        else:
            continue
        blues = [(r, c) for (r, c) in coords if grid[r][c] == 1]
        for i, (r, c) in enumerate(blues):
            out[r][c] = 2 if i % 2 == 0 else 3
    return out