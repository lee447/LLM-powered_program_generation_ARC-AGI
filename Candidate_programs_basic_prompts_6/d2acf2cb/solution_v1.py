from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    mapcol = {0: 8, 6: 7, 8: 0, 7: 6}
    row4 = {r: [c for c, v in enumerate(grid[r]) if v == 4] for r in range(m)}
    rects = []
    rows = sorted([r for r, cols in row4.items() if len(cols) >= 2])
    for i, r1 in enumerate(rows):
        for r2 in rows[i+1:]:
            for j in range(len(row4[r1])):
                for k in range(j+1, len(row4[r1])):
                    c1, c2 = row4[r1][j], row4[r1][k]
                    if c2 - c1 > 1 and grid[r2][c1] == 4 and grid[r2][c2] == 4:
                        rects.append((r1, r2, c1, c2))
    for r1, r2, c1, c2 in rects:
        for r in range(r1+1, r2):
            for c in (c1, c2):
                v = grid[r][c]
                if v in mapcol:
                    out[r][c] = mapcol[v]
    for r, cols in row4.items():
        for i in range(len(cols)):
            for j in range(i+1, len(cols)):
                c1, c2 = cols[i], cols[j]
                if c2 - c1 > 1 and not any(r in (R1, R2) and c1 == C1 and c2 == C2 for R1, R2, C1, C2 in rects):
                    for c in range(c1+1, c2):
                        v = grid[r][c]
                        if v in mapcol:
                            out[r][c] = mapcol[v]
    return out