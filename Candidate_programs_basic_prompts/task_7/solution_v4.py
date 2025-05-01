def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [r for r in range(h) if all(grid[r][c] == grid[r][0] for c in range(w))]
    cols = [c for c in range(w) if all(grid[r][c] == grid[0][c] for r in range(h))]
    bar = grid[rows[0]][0]
    bh = rows[1] - rows[0] - 1
    bw = cols[1] - cols[0] - 1
    blocks_r = [(rows[i] + 1, rows[i+1]) for i in range(len(rows)-1)]
    blocks_c = [(cols[j] + 1, cols[j+1]) for j in range(len(cols)-1)]
    vals = set()
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != 1 and v != bar:
                vals.add(v)
    seed_color = vals.pop() if vals else None
    seed_block = None
    for bi,(rs,re) in enumerate(blocks_r):
        for bj,(cs,ce) in enumerate(blocks_c):
            found = any(grid[r][c] == seed_color for r in range(rs,re) for c in range(cs,ce))
            if found:
                seed_block = (bi,bj)
                break
        if seed_block: break
    sr, sc = blocks_r[seed_block[0]][0], blocks_c[seed_block[1]][0]
    offsets = [(r-sr, c-sc) for r in range(sr, sr+bh) for c in range(sc, sc+bw) if grid[r][c] == seed_color]
    out = [row[:] for row in grid]
    for bi,(rs,re) in enumerate(blocks_r):
        for bj,(cs,ce) in enumerate(blocks_c):
            if (bi,bj) == seed_block: continue
            for dr,dc in offsets:
                r, c = rs+dr, cs+dc
                if 0 <= r < h and 0 <= c < w and grid[r][c] == 1:
                    out[r][c] = seed_color
    return out