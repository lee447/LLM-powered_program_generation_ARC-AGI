from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    stroke_col = min(j for j in range(w) if sum(grid[r][j] != 0 for r in range(h)) > 1)
    stroke_rows = [r for r in range(h) if grid[r][stroke_col] != 0]
    if not stroke_rows:
        return grid
    r0, r1 = min(stroke_rows), max(stroke_rows)
    active = [any(grid[r][j] != 0 for r in range(r0, r1+1)) for j in range(stroke_col+1, w)]
    clusters = []
    j = stroke_col+1
    while j < w:
        if j-stroke_col-1 < len(active) and active[j-stroke_col-1]:
            start = j
            while j < w and j-stroke_col-1 < len(active) and active[j-stroke_col-1]:
                j += 1
            clusters.append((start, j - start))
        else:
            j += 1
    if not clusters:
        return grid
    maxw = max(width for _, width in clusters)
    out = [row[:] for row in grid]
    for start, ow in clusters:
        seg = [r for r in range(r0, r1+1) if any(grid[r][c] != 0 for c in range(start, start+ow))]
        seg.sort()
        if not seg:
            continue
        tile_all = True
        if seg[0] == r0 and len(seg) > 1:
            tile_all = False
        special = (seg[0] == r0 and len(seg) == 1 and start == stroke_col+1)
        H = len(seg) if seg else 1
        for r in range(r0, r1+1):
            if special:
                v = grid[r][stroke_col]
                for k in range(maxw):
                    out[r][start+k] = v
            elif tile_all:
                idx = (r - r0) % H
                pr = seg[idx]
                for k in range(maxw):
                    if ow == maxw:
                        val = grid[pr][start+k]
                    else:
                        if k < ow:
                            val = grid[pr][start+k]
                            if val == 0:
                                val = grid[pr][start]
                        else:
                            val = grid[pr][start]
                    out[r][start+k] = val
            else:
                if r in seg:
                    for k in range(maxw):
                        if ow == maxw:
                            val = grid[r][start+k]
                        else:
                            val = grid[r][start]
                        out[r][start+k] = val
    return out