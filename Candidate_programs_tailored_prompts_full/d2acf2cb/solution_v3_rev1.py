from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    anchors = {}
    for r in range(h):
        cols = [c for c, v in enumerate(grid[r]) if v == 4]
        if len(cols) >= 2:
            c1, c2 = cols[0], cols[1]
            anchors.setdefault((c1, c2), []).append(r)
    for (c1, c2), rows in anchors.items():
        rows.sort()
        if len(rows) == 1:
            r = rows[0]
            vals = []
            for c in range(c1+1, c2):
                v = grid[r][c]
                if v not in vals:
                    vals.append(v)
            if len(vals) == 2:
                m0, m1 = vals[0], vals[1]
                ic = [8, 7]
                for c in range(c1+1, c2):
                    v = grid[r][c]
                    out[r][c] = ic[0] if v == m0 else ic[1]
        elif len(rows) > 2:
            r0 = rows[0]
            vals = []
            for c in range(c1+1, c2):
                v = grid[r0][c]
                if v not in vals:
                    vals.append(v)
            if len(vals) == 2:
                ic_map = {vals[0]: vals[1], vals[1]: vals[0]}
                for r in rows:
                    for c in range(c1+1, c2):
                        v = grid[r][c]
                        if v in ic_map:
                            out[r][c] = ic_map[v]
        else:
            r0, r1 = rows[0], rows[1]
            for r in range(r0+1, r1):
                if r == r1-1:
                    out[r][c1] = 7
                else:
                    out[r][c1] = 8
                if r == r0+1 or r == r1-1:
                    out[r][c2] = 8
                else:
                    out[r][c2] = 7
    return out