from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    minr, maxr = h, -1
    minc, maxc = w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    rh = maxr - minr + 1
    cw = maxc - minc + 1
    th, tw = rh // 2, cw // 2
    tl = [grid[minr + i][minc:minc + tw] for i in range(th)]
    def transform(tile, kind):
        if kind == 'ID': return [row[:] for row in tile]
        if kind == 'H': return [row[::-1] for row in tile]
        if kind == 'V': return tile[::-1]
        if kind == 'B': return [row[::-1] for row in tile[::-1]]
    out = [[0]*w for _ in range(h)]
    # TL
    for i in range(th):
        for j in range(tw):
            out[minr+i][minc+j] = grid[minr+i][minc+j]
    # other tiles
    quads = [
        (minr, minc+tw, 'H'),
        (minr+th, minc, 'V'),
        (minr+th, minc+tw, 'B')
    ]
    for sr, sc, kind in quads:
        pat = transform(tl, kind)
        mapping = {}
        for i in range(th):
            for j in range(tw):
                v = grid[sr+i][sc+j]
                if v != 0:
                    mapping[pat[i][j]] = v
        for i in range(th):
            for j in range(tw):
                val = mapping.get(pat[i][j], 0)
                out[sr+i][sc+j] = val
    return out