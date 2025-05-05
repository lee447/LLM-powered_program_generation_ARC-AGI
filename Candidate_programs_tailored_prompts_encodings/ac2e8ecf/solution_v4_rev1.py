from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rings = []
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v == 0:
                continue
            for s in (3, 4):
                if i + s > h or j + s > w:
                    continue
                ok = True
                for k in range(s):
                    if grid[i][j + k] != v or grid[i + s - 1][j + k] != v or grid[i + k][j] != v or grid[i + k][j + s - 1] != v:
                        ok = False
                        break
                if not ok:
                    continue
                for ii in range(i + 1, i + s - 1):
                    for jj in range(j + 1, j + s - 1):
                        if grid[ii][jj] != 0:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    rings.append({'x': j, 'y': i, 'size': s, 'v': v})
    bycol = {}
    for r in rings:
        bycol.setdefault(r['v'], []).append(r)
    keep = []
    for v, group in bycol.items():
        m = max(r['size'] for r in group)
        for r in group:
            if r['size'] == m:
                keep.append(r)
    small = sorted([r for r in keep if r['size'] == 3], key=lambda r: r['x'])
    large = sorted([r for r in keep if r['size'] == 4], key=lambda r: r['x'])
    out = [[0] * w for _ in range(h)]
    y0 = 0
    x0 = 1
    for r in small:
        for k in range(r['size']):
            out[y0][x0 + k] = r['v']
            out[y0 + r['size'] - 1][x0 + k] = r['v']
            out[y0 + k][x0] = r['v']
            out[y0 + k][x0 + r['size'] - 1] = r['v']
        x0 += r['size'] + 1
    if small:
        y1 = max(r['size'] for r in small)
    else:
        y1 = 0
    x1 = 1
    for r in large:
        for k in range(r['size']):
            out[y1][x1 + k] = r['v']
            out[y1 + r['size'] - 1][x1 + k] = r['v']
            out[y1 + k][x1] = r['v']
            out[y1 + k][x1 + r['size'] - 1] = r['v']
        x1 += r['size'] + 1
    return out