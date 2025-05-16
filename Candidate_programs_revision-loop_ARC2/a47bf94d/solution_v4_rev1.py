from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    counts = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c:
                counts[c] = counts.get(c, 0) + 1
    for c, cnt in counts.items():
        if cnt == 9:
            pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == c]
            rs = [i for i, _ in pts]; cs = [j for _, j in pts]
            i0, i1 = min(rs), max(rs); j0, j1 = min(cs), max(cs)
            if i1 - i0 == 2 and j1 - j0 == 2:
                for i in range(i0, i1+1):
                    for j in range(j0, j1+1):
                        out[i][j] = 0
                out[i0][j0+1] = c
                out[i0+1][j0] = c
                out[i0+1][j0+2] = c
                out[i0+2][j0+1] = c
    return out