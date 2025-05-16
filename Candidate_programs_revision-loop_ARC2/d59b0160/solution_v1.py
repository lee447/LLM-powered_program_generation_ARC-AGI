def solve(grid):
    n = len(grid)
    b = n // 4
    bg = 7
    out = [[bg]*n for _ in range(n)]
    for bi in range(4):
        for bj in range(4):
            counts = {}
            for i in range(bi*b, bi*b+b):
                for j in range(bj*b, bj*b+b):
                    c = grid[i][j]
                    if c != bg:
                        counts[c] = counts.get(c,0)+1
            if not counts:
                keep = False
            else:
                m = max(counts.values())
                keep = any(v==m and list(counts.keys())[k]==c for k,(c,v) in enumerate(counts.items()))
            if keep:
                for i in range(bi*b, bi*b+b):
                    for j in range(bj*b, bj*b+b):
                        out[i][j] = grid[i][j]
    return out