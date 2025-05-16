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

    if any(all(v == sep for v in row) for row in grid):
        blocks = split_rows(grid)
        mask = next(b for b in blocks if any(c == 0 for row in b for c in row) and any(c != 0 for row in b for c in row))
        uni = [b for b in blocks if all(c != 0 for row in b for c in row)]
        r1, r2 = uni[0], uni[1]
        mh, mw = len(mask), len(mask[0])
        rs = [i for i in range(mh) if any(mask[i][j] != 0 for j in range(mw))]
        cs = [j for j in range(mw) if any(mask[i][j] != 0 for i in range(mh))]
        sub = [[mask[i][j] for j in cs] for i in rs]
        h1, h2 = len(r1), len(r2)
        out_h, out_w = h1 + h2 - len(rs), len(cs)
        c1 = next(c for row in r1 for c in row if c != 0)
        c2 = next(c for row in r2 for c in row if c != 0)
        out = [[0]*out_w for _ in range(out_h)]
        for i in range(out_h):
            if i < h1 - len(rs):
                for j in range(out_w):
                    out[i][j] = c1
            elif i < h1:
                mi = i - (h1 - len(rs))
                for j in range(out_w):
                    out[i][j] = c2 if sub[mi][j] != 0 else c1
            else:
                for j in range(out_w):
                    out[i][j] = c2
        return out
    else:
        blocks = split_cols(grid)
        mask = next(b for b in blocks if any(c == 0 for row in b for c in row) and any(c != 0 for row in b for c in row))
        uni = [b for b in blocks if all(c != 0 for row in b for c in row)]
        r1, r2 = uni[0], uni[1]
        mh, mw = len(mask), len(mask[0])
        rs = [i for i in range(mh) if any(mask[i][j] != 0 for j in range(mw))]
        cs = [j for j in range(mw) if any(mask[i][j] != 0 for i in range(mh))]
        sub = [[mask[i][j] for j in cs] for i in rs]
        w1, w2 = len(r1[0]), len(r2[0])
        out_h, out_w = len(rs), w1 + w2 + len(cs)
        c1 = next(c for row in r1 for c in row if c != 0)
        c2 = next(c for row in r2 for c in row if c != 0)
        out = [[0]*out_w for _ in range(out_h)]
        for i in range(out_h):
            for j in range(out_w):
                if j < w1:
                    out[i][j] = c1
                elif j < w1 + len(cs):
                    out[i][j] = c2 if sub[i][j - w1] != 0 else c1
                else:
                    out[i][j] = c2
        return out