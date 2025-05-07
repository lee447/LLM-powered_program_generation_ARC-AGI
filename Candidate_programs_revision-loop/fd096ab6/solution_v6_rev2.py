import math
from collections import Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(c for row in grid for c in row)
    bg = max(counts, key=counts.get)
    out = [row[:] for row in grid]
    for c, cnt in counts.items():
        if c == bg or cnt >= 5:
            continue
        pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == c]
        cx = sum(i for i, _ in pts) / len(pts)
        cy = sum(j for _, j in pts) / len(pts)
        n_add = 5 - len(pts)
        cand = []
        for i, j in pts:
            dx, dy = i - cx, j - cy
            for rx, ry in ((dy, -dx), (-dx, -dy), (-dy, dx)):
                ni, nj = cx + rx, cy + ry
                ri, rj = int(round(ni)), int(round(nj))
                if 0 <= ri < h and 0 <= rj < w and out[ri][rj] != c:
                    cand.append((ri, rj))
        ci, cj = int(round(cx)), int(round(cy))
        if 0 <= ci < h and 0 <= cj < w and out[ci][cj] != c:
            cand.append((ci, cj))
        seen = set(pts)
        added = 0
        for i, j in sorted(cand, key=lambda x:(abs(x[0]-cx)+abs(x[1]-cy), x[0], x[1])):
            if added >= n_add:
                break
            if (i, j) not in seen:
                out[i][j] = c
                seen.add((i, j))
                added += 1
    return out