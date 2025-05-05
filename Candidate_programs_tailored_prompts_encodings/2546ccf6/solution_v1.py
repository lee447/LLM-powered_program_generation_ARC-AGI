def solve(grid):
    H, W = len(grid), len(grid[0])
    stripe_rows = [r for r in range(H) if all(grid[r][c] != 0 for c in range(W))]
    stripe_cols = [c for c in range(W) if all(grid[r][c] != 0 for r in range(H))]
    y_edges = [-1] + stripe_rows + [H]
    x_edges = [-1] + stripe_cols + [W]
    def find_block(r, edges):
        for i in range(len(edges) - 1):
            if edges[i] < r < edges[i+1]:
                return i
    pattern = {}
    for r in range(H):
        if r in stripe_rows: continue
        for c in range(W):
            v = grid[r][c]
            if v == 0 or c in stripe_cols: continue
            br = find_block(r, y_edges)
            bc = find_block(c, x_edges)
            pattern.setdefault(v, {}).setdefault((br, bc), []).append((r, c))
    nb_r = len(y_edges) - 1
    nb_c = len(x_edges) - 1
    out = [row[:] for row in grid]
    for v, blocks in pattern.items():
        brs = sorted({b for b,_ in blocks})
        bcs = sorted({d for _,d in blocks})
        if len(brs) == 1:
            b0 = brs[0]
            brs = [b0, min(b0+1, nb_r-1)]
        if len(bcs) == 1:
            c0 = bcs[0]
            bcs = [c0, min(c0+1, nb_c-1)]
        br0, bc0 = min(brs), min(bcs)
        ref = blocks[(br0, bc0)]
        oy = y_edges[br0] + 1
        ox = x_edges[bc0] + 1
        deltas = [(r-oy, c-ox) for r,c in ref]
        for br in brs:
            for bc in bcs:
                base_r = y_edges[br] + 1
                base_c = x_edges[bc] + 1
                if (br, bc) in blocks: continue
                for dy, dx in deltas:
                    out[base_r+dy][base_c+dx] = v
    return out