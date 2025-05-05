import numpy as np
def solve(grid):
    H, W = len(grid), len(grid[0])
    stripe_rows = [r for r in range(H) if len(set(grid[r]))==1 and grid[r][0]!=0]
    stripe_cols = [c for c in range(W) if len({grid[r][c] for r in range(H)})==1 and grid[0][c]!=0]
    y_edges = [-1] + stripe_rows + [H]
    x_edges = [-1] + stripe_cols + [W]
    def find_block(idx, edges):
        for i in range(len(edges)-1):
            if edges[i] < idx < edges[i+1]:
                return i
    blocks = {}
    for r in range(H):
        if r in stripe_rows: continue
        for c in range(W):
            if c in stripe_cols: continue
            v = grid[r][c]
            if v==0: continue
            br = find_block(r, y_edges)
            bc = find_block(c, x_edges)
            blocks.setdefault(v, {}).setdefault((br,bc), []).append((r,c))
    out = [row[:] for row in grid]
    for v, bdict in blocks.items():
        brs = sorted({br for br,bc in bdict})
        bcs = sorted({bc for br,bc in bdict})
        br0, bc0 = brs[0], bcs[0]
        ref = bdict[(br0,bc0)]
        oy0 = y_edges[br0]+1
        ox0 = x_edges[bc0]+1
        deltas = [(r-oy0, c-ox0) for r,c in ref]
        for br in brs:
            for bc in bcs:
                if (br,bc) in bdict: continue
                oy = y_edges[br]+1
                ox = x_edges[bc]+1
                for dy,dx in deltas:
                    out[oy+dy][ox+dx] = v
    return out