from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep = 1
    def split_rows(g):
        parts, i = [], 0
        while i < len(g):
            if all(v == sep for v in g[i]):
                i += 1
            else:
                j = i
                while j < len(g) and not all(v == sep for v in g[j]):
                    j += 1
                parts.append(g[i:j])
                i = j
        return parts
    def split_cols(g):
        parts, j = [], 0
        while j < len(g[0]):
            if all(row[j] == sep for row in g):
                j += 1
            else:
                k = j
                while k < len(g[0]) and not all(row[k] == sep for row in g):
                    k += 1
                parts.append([row[j:k] for row in g])
                j = k
        return parts
    horiz = any(all(v == sep for v in row) for row in grid)
    if horiz:
        blocks = split_rows(grid)
        nz = [b for b in blocks if any(c != 0 for row in b for c in row)]
        mb = next(b for b in nz if any(c == 0 for row in b for c in row))
        idx = nz.index(mb)
        r1, r2 = nz[idx+1], nz[idx+2]
        mh, mw = len(mb), len(mb[0])
        rs = [i for i in range(mh) if any(mb[i][j] != 0 for j in range(mw))]
        cs = [j for j in range(mw) if any(mb[i][j] != 0 for i in range(mh))]
        mask = [[mb[i][j] for j in cs] for i in rs]
        r1c = next(c for row in r1 for c in row if c != 0)
        r2c = next(c for row in r2 for c in row if c != 0)
        out_h = len(r1) + len(r2) - len(rs)
        out_w = len(cs)
        out = [[0]*out_w for _ in range(out_h)]
        for i in range(out_h):
            for j in range(out_w):
                out[i][j] = r2c if mask[i % len(rs)][j] != 0 else r1c
        return out
    else:
        blocks = split_cols(grid)
        nz = [b for b in blocks if any(c != 0 for row in b for c in row)]
        mb = next(b for b in nz if any(c == 0 for row in b for c in row))
        idx = nz.index(mb)
        r1, r2 = nz[idx+1], nz[idx+2]
        mh, mw = len(mb), len(mb[0])
        rs = [i for i in range(mh) if any(mb[i][j] != 0 for j in range(mw))]
        cs = [j for j in range(mw) if any(mb[i][j] != 0 for i in range(mh))]
        mask = [[mb[i][j] for j in cs] for i in range(mh) for _ in ()]  # preserve rows
        mask = [mask[i] for i in rs]
        r1c = next(c for row in r1 for c in row if c != 0)
        r2c = next(c for row in r2 for c in row if c != 0)
        out_h = len(rs)
        out_w = len(r1[0]) + len(r2[0]) + len(cs)
        out = [[0]*out_w for _ in range(out_h)]
        for i in range(out_h):
            for j in range(out_w):
                out[i][j] = r2c if mask[i][j % len(cs)] != 0 else r1c
        return out