from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    shape_coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not shape_coords:
        return [row[:] for row in grid]
    minr = min(r for r, c in shape_coords)
    maxr = max(r for r, c in shape_coords)
    minc = min(c for r, c in shape_coords)
    maxc = max(c for r, c in shape_coords)
    h0, w0 = maxr - minr + 1, maxc - minc + 1
    mask = [[grid[minr + i][minc + j] == 8 for j in range(w0)] for i in range(h0)]
    def rot90(m):
        return [list(row) for row in zip(*m[::-1])]
    masks = []
    m = mask
    for _ in range(4):
        masks.append(m)
        m = rot90(m)
    out = [row[:] for row in grid]
    for m in masks:
        mh, mw = len(m), len(m[0])
        for i in range(h - mh + 1):
            for j in range(w - mw + 1):
                ok = True
                for ii in range(mh):
                    for jj in range(mw):
                        if m[ii][jj] and grid[i+ii][j+jj] != 0:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    for ii in range(mh):
                        for jj in range(mw):
                            if m[ii][jj]:
                                out[i+ii][j+jj] = 8
    return out