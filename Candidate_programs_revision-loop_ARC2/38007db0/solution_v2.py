def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    sep_cols = [c for c in range(cols) if all(grid[r][c] == grid[0][c] for r in range(rows))]
    segs = [(sep_cols[i], sep_cols[i+1]) for i in range(len(sep_cols)-1)]
    best = min(segs, key=lambda se: sum(grid[r][c] for r in range(rows) for c in range(se[0], se[1]+1)))
    c0, c1 = best
    return [[grid[r][c] for c in range(c0, c1+1)] for r in range(rows)]