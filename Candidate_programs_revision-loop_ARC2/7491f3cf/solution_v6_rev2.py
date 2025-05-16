from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    stripes = [x for x in range(w) if all(grid[y][x] == border for y in range(h))]
    bw = stripes[1] - stripes[0] - 1
    blocks = [(stripes[i] + 1, stripes[i+1] - 1) for i in range(len(stripes) - 1)]
    res = [row[:] for row in grid]
    for x0, x1 in blocks:
        coords = {}
        for y in range(1, h-1):
            for x in range(x0, x1+1):
                c = grid[y][x]
                if c != border:
                    coords.setdefault(c, []).append((y, x))
        for c, ps in coords.items():
            if not ps or len(ps) == 2*bw-1:
                continue
            rel = [(y-1, x-x0) for y, x in ps]
            ys = [ry for ry, rx in rel]
            xs = [rx for ry, rx in rel]
            if len(ps) == bw and len(set(xs)) == 1:
                cy = 1 + bw//2
                for dx in range(bw):
                    res[cy][x0+dx] = c
            elif len(ps) == bw and len(set(ys)) == 1:
                cx = bw//2
                for dy in range(bw):
                    res[1+dy][x0+cx] = c
            else:
                main = all(ry == rx for ry, rx in rel)
                anti = all(ry + rx == bw-1 for ry, rx in rel)
                if main:
                    for i in range(bw):
                        res[1+i][x0+(bw-1-i)] = c
                elif anti:
                    for i in range(bw):
                        res[1+i][x0+i] = c
    return res