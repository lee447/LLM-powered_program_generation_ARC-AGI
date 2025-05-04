def solve(grid):
    row = grid[0]
    N = len(row)
    j = next(i for i,v in enumerate(row) if v!=0)
    out = [[0]*N for _ in range(N)]
    C = row[j]
    for k in range(j+1):
        out[k][j-k] = C
        out[k][j+k] = C
    pts = [(r, j-r) for r in range(j+1)] + [(r, j+r) for r in range(j+1)]
    for r,c in pts:
        dr, dc = r-j, c-j
        for dr2, dc2 in (( dc, dr), (-dr, -dc), (-dc, -dr)):
            r2, c2 = j+dr2, j+dc2
            if 0<=r2<N and 0<=c2<N and out[r2][c2]==0:
                out[r2][c2] = 1
    return out