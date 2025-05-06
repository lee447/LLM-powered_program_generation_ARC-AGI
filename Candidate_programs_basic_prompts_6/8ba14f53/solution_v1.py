from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = []
    for bi in range(3):
        # extract block
        bx = [row[3*bi:3*bi+3] for row in grid]
        # collect nonzero positions by color
        pos = {}
        for i in range(len(bx)):
            for j in range(3):
                c = bx[i][j]
                if c != 0:
                    pos.setdefault(c, []).append((i, j))
        if not pos:
            out.append([0, 0, 0])
            continue
        # choose a color for summary
        chosen = None
        summary = None
        # horizontal test: any color has ≥2 in same row
        for c, coords in pos.items():
            rows = {}
            for i, _ in coords:
                rows[i] = rows.get(i, 0) + 1
            if any(cnt >= 2 for cnt in rows.values()):
                chosen = c
                summary = [c, c, c]
                break
        if summary:
            out.append(summary)
            continue
        # vertical test: any color has ≥2 in same col
        for c, coords in pos.items():
            cols = {}
            for _, j in coords:
                cols[j] = cols.get(j, 0) + 1
            if any(cnt >= 2 for cnt in cols.values()):
                chosen = c
                summary = [c, 0, 0]
                break
        if summary:
            out.append(summary)
            continue
        # corner case: pick the color with most pixels
        chosen = max(pos.items(), key=lambda x: len(x[1]))[0]
        out.append([chosen, chosen, 0])
    return out