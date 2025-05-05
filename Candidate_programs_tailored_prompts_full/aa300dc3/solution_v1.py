def solve(grid):
    h=len(grid); w=len(grid[0])
    row_to_cols={}
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0:
                row_to_cols.setdefault(r,set()).add(c)
    b_map={1:{},-1:{}}
    for r,cols in row_to_cols.items():
        for c in cols:
            for s in (1,-1):
                b=c-s*r
                if b not in b_map[s]: b_map[s][b]=set()
                b_map[s][b].add(r)
    best_s,best_b,best_n=0,0,0
    for s in (1,-1):
        for b,rows in b_map[s].items():
            n=len(rows)
            if n>best_n:
                best_n, best_s, best_b = n, s, b
    out=[row[:] for row in grid]
    for r in b_map[best_s][best_b]:
        c=best_s*r+best_b
        if 0<=r<h and 0<=c<w and grid[r][c]==0:
            out[r][c]=8
    return out