from collections import Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(c for row in grid for c in row)
    bg = max(counts, key=counts.get)
    out = [row[:] for row in grid]
    for c, cnt in counts.items():
        if c == bg or cnt == 5:
            continue
        pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == c]
        n_add = 5 - len(pts)
        cx = sum(i for i, _ in pts) / len(pts)
        cy = sum(j for _, j in pts) / len(pts)
        cand = set()
        for i, j in pts:
            dx, dy = i - cx, j - cy
            for dx2, dy2 in ((dy, -dx), (-dy, dx)):
                ni, nj = cx + dx2, cy + dy2
                ri, rj = int(round(ni)), int(round(nj))
                if 0 <= ri < h and 0 <= rj < w and grid[ri][rj] != c:
                    cand.add((ri, rj))
        ci, cj = int(round(cx)), int(round(cy))
        if 0 <= ci < h and 0 <= cj < w and grid[ci][cj] != c:
            cand.add((ci, cj))
        for i, j in sorted(cand)[:n_add]:
            out[i][j] = c
    return out