from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else 0
    shapes = []
    for i in range(h - 3):
        for j in range(w - 3):
            c = grid[i][j]
            if c == 0: continue
            ok = True
            for dj in range(4):
                if grid[i][j+dj] != c or grid[i+3][j+dj] != c:
                    ok = False; break
            if not ok: continue
            for di in range(4):
                if grid[i+di][j] != c or grid[i+di][j+3] != c:
                    ok = False; break
            if not ok: continue
            if grid[i+1][j+1] or grid[i+1][j+2] or grid[i+2][j+1] or grid[i+2][j+2]:
                continue
            blk = [row[j:j+4] for row in grid[i:i+4]]
            shapes.append((i, j, blk))
    if not shapes:
        return []
    band_h = h // 3 if h >= 3 else h
    bands = {0: [], 1: [], 2: []}
    for i, j, blk in shapes:
        b = i // band_h if band_h else 0
        if b >= 3: b = 2
        bands[b].append((j, blk, b))
    max_count = max(len(bands[b]) for b in bands)
    sel_bands = [b for b in bands if len(bands[b]) == max_count]
    sel = []
    for b in sel_bands:
        sel += bands[b]
    if max_count > 1 and len(sel_bands) > 1 and any(len(bands[b]) > 1 for b in sel_bands):
        sel.sort(key=lambda x: x[0])
        acc = []
        for j, blk, b in sel:
            if not acc or j >= acc[-1][0] + 4:
                acc.append((j, blk, b))
            else:
                lj, lblk, lb = acc[-1]
                if b > lb:
                    acc[-1] = (j, blk, b)
        sel = acc
    else:
        sel.sort(key=lambda x: x[0])
    out = []
    for di in range(4):
        row = []
        for j, blk, b in sel:
            row += blk[di]
        out.append(row)
    return out