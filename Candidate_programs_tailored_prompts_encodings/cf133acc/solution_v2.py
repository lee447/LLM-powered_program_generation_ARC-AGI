def solve(grid):
    H, W = len(grid), len(grid[0])
    bar_rows = [r for r in range(H) if sum(1 for c in grid[r] if c) > 2]
    a = [j for j in range(W) if all(grid[r][j] == 0 for r in bar_rows) and any(grid[r][j] != 0 for r in range(H) if r not in bar_rows)]
    a1, a2 = sorted(a)[:2]
    mid = bar_rows[len(bar_rows)//2]
    left_info = {}
    right_info = {}
    for r in bar_rows:
        L = [j for j in range(W) if j != a1 and j < a2 and grid[r][j]]
        R = [j for j in range(W) if j != a2 and j > a1 and grid[r][j]]
        left_info[r] = (grid[r][L[0]], len(L))
        right_info[r] = (grid[r][R[0]], len(R))
    botL = [(r, grid[r][a1]) for r in range(mid+1, H) if grid[r][a1]]
    botR = [(r, grid[r][a2]) for r in range(mid+1, H) if grid[r][a2]]
    out = [[0]*W for _ in range(H)]
    for r in range(H):
        if r in bar_rows and r > mid:
            out[r] = grid[r][:]
    seqL = []
    seqR = []
    for r in bar_rows:
        cL, nL = left_info[r]
        cR, nR = right_info[r]
        seqL += [cL]*nL
        seqR += [cR]*nR
    for i, c in enumerate(seqL):
        out[i][a1] = c
    for i, c in enumerate(seqR):
        out[i][a2] = c
    for r in bar_rows:
        out[r][a1], out[r][a2] = left_info[r][0], right_info[r][0]
    bl = len(botL)
    for i, (_, c) in enumerate(botL):
        out[mid+1+i][a1] = c
    for i, (_, c) in enumerate(botR):
        out[mid+1+i][a2] = c
    return out