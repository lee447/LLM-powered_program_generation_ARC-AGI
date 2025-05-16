from collections import Counter
def solve(grid):
    def transpose(g):
        return [list(row) for row in zip(*g)]
    def vs(g):
        h, w = len(g), len(g[0])
        ls_col = 0
        while ls_col < w and all(g[r][ls_col] == g[0][ls_col] for r in range(h)):
            ls_col += 1
        rs_col = 0
        while rs_col < w and all(g[r][w-1-rs_col] == g[0][w-1-rs_col] for r in range(h)):
            rs_col += 1
        border = [c for c in range(w) if all(g[r][c] == 4 for r in range(h))]
        bs, be = min(border), max(border)
        a0, a1 = ls_col, bs - 1
        b0, b1 = be + 1, w - rs_col - 1
        ra = [g[r][c] for r in range(h) for c in range(a0, a1+1)]
        rb = [g[r][c] for r in range(h) for c in range(b0, b1+1)]
        ba = Counter(ra).most_common(1)[0][0]
        bb = Counter(rb).most_common(1)[0][0]
        out = [row[:] for row in g]
        for r in range(h):
            for c in range(b0, b1+1):
                out[r][c] = bb
        for r in range(h):
            for c in range(a0, a1+1):
                v = g[r][c]
                if v != ba:
                    c2 = b0 + (a1 - c)
                    out[r][c2] = v
        return out
    if all(grid[r][0] == grid[0][0] for r in range(len(grid))):
        return vs(grid)
    else:
        t = transpose(grid)
        u = vs(t)
        return transpose(u)