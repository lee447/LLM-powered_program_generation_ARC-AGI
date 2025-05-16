from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    counts = Counter(v for row in grid for v in row)
    bg = counts.most_common(1)[0][0]
    shape = next(c for c, _ in counts.most_common() if c != bg)
    pts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == shape]
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    maxc_global = max(c for _, c in pts)
    best = None
    best_area = rows * cols + 1
    anchors = [c for c in range(cols) if grid[minr][c] == shape]
    for c0 in anchors:
        maxw = maxc_global - c0 + 1
        maxh = maxr - minr + 1
        for h in range(2, maxh + 1):
            for w in range(2, maxw + 1):
                if grid[minr][c0] != shape: continue
                if any(c0 + w - 1 >= cols):
                    continue
                tile = [row[c0:c0 + w] for row in grid[minr:minr + h]]
                if tile[0][0] != shape: continue
                ok = True
                for r, c in pts:
                    ri = (r - minr) % h
                    cj = (c - c0) % w
                    if tile[ri][cj] != shape:
                        ok = False
                        break
                if not ok:
                    continue
                for r in range(rows):
                    for c in range(cols):
                        ri = (r - minr) % h
                        cj = (c - c0) % w
                        if tile[ri][cj] == shape and grid[r][c] != shape:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                area = h * w
                if area < best_area:
                    best_area = area
                    best = (h, w, minr, c0)
    if best is None:
        return []
    h, w, r0, c0 = best
    return [row[c0:c0 + w] for row in grid[r0:r0 + h]]