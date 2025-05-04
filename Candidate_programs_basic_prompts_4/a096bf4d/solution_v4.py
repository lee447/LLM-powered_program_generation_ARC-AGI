def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(c == 0 for c in grid[i])]
    sep_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    block_h = sep_rows[1] - sep_rows[0] - 1
    block_w = sep_cols[1] - sep_cols[0] - 1
    counts = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v not in (0, 1):
                counts[v] = counts.get(v, 0) + 1
    rare = [v for v, c in counts.items() if c == 2]
    mapping = []
    for v in rare:
        for i in range(h):
            for j in range(w):
                if grid[i][j] == v:
                    br = next(b for b in range(len(sep_rows) - 1) if sep_rows[b] < i < sep_rows[b+1])
                    bc = next(b for b in range(len(sep_cols) - 1) if sep_cols[b] < j < sep_cols[b+1])
                    r0 = sep_rows[br] + 1
                    c0 = sep_cols[bc] + 1
                    dr, dc = i - r0, j - c0
                    mapping.append((v, br, bc, dr, dc))
    out = [row[:] for row in grid]
    B = len(sep_rows) - 1
    C = len(sep_cols) - 1
    for v, br0, bc0, dr, dc in mapping:
        for br in range(B):
            for bc in range(C):
                if br == br0:
                    r = sep_rows[br] + 1 + dr
                    c = sep_cols[bc] + 1 + dc
                    out[r][c] = v
    return out