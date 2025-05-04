def solve(grid):
    n = len(grid)
    m = len(grid[0])
    A = next(grid[i][j] for i in range(n) for j in range(m) if grid[i][j] != 0)
    B = 9 - A
    coords = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == A]
    top = min(i for i, _ in coords)
    bot = max(i for i, _ in coords)
    lef = min(j for _, j in coords)
    rig = max(j for _, j in coords)
    h, w = bot - top + 1, rig - lef + 1
    bc_r, bc_c = (top + bot) / 2, (lef + rig) / 2
    gc_r, gc_c = (n - 1) / 2, (m - 1) / 2
    out = [[0]*m for _ in range(n)]
    for k in range(4):
        col = A if k % 2 == 0 else B
        for i, j in coords:
            dr, dc = i - bc_r, j - bc_c
            if k == 1:
                dr, dc = -dc, dr
            elif k == 2:
                dr, dc = -dr, -dc
            elif k == 3:
                dr, dc = dc, -dr
            ii = int(round(gc_r + dr))
            jj = int(round(gc_c + dc))
            if 0 <= ii < n and 0 <= jj < m:
                out[ii][jj] = col
    return out