from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    frames = []
    for i in range(h):
        for j in range(w):
            if i + 3 < h and j + 3 < w:
                ok = True
                for x in range(4):
                    if grid[i][j+x] != 1 or grid[i+3][j+x] != 1 or grid[i+x][j] != 1 or grid[i+x][j+3] != 1:
                        ok = False
                        break
                if ok:
                    interior = (grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j+1], grid[i+2][j+2])
                    frames.append((i, j, interior))
    frame_h = frame_w = 4
    rows = sorted({i for i, _, _ in frames})
    cols = sorted({j for _, j, _ in frames})
    def cluster(coords, th):
        res = []
        curr = [coords[0]]
        for x in coords[1:]:
            if x - curr[-1] <= th:
                curr.append(x)
            else:
                res.append(curr)
                curr = [x]
        res.append(curr)
        return res
    row_clusters = cluster(rows, frame_h)
    col_clusters = cluster(cols, frame_w)
    fmap = {(i, j): ints for i, j, ints in frames}
    out = [row[:] for row in grid]
    def rot2(m): return (m[2], m[0], m[3], m[1])
    def rot_k(m, k):
        for _ in range(k): m = rot2(m)
        return m
    for rc in row_clusters:
        for cc in col_clusters:
            fc = [(i, j, fmap[(i, j)]) for i in rc for j in cc if (i, j) in fmap]
            if len(fc) != len(rc) * len(cc): continue
            counts = {}
            for _, _, ints in fc:
                counts[ints] = counts.get(ints, 0) + 1
            for i, j, ints in fc:
                if counts[ints] == 1:
                    ti, tj, tpl = i, j, ints
                    break
            for i, j, _ in fc:
                r = rc.index(i)
                c = cc.index(j)
                tr = rc.index(ti)
                tc = cc.index(tj)
                k = ((c - tc) - (r - tr)) % 4
                m = rot_k(tpl, k)
                out[i+1][j+1] = m[0]
                out[i+1][j+2] = m[1]
                out[i+2][j+1] = m[2]
                out[i+2][j+2] = m[3]
    return out