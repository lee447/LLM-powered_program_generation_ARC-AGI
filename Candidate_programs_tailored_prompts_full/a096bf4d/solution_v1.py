def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_seps = [i for i in range(h) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_regions = [(row_seps[i]+1, row_seps[i+1]-1) for i in range(len(row_seps)-1)]
    col_regions = [(col_seps[j]+1, col_seps[j+1]-1) for j in range(len(col_seps)-1)]
    out = [row[:] for row in grid]
    for ri, (r0, r1) in enumerate(row_regions):
        H = r1 - r0 + 1
        dlr = H//2 + (H%2)
        forci = col_regions[0][0] + (col_regions[0][1]-col_regions[0][0]+1)//2 - 1  # placeholder
        W = col_regions[0][1] - col_regions[0][0] + 1
        dlc = W//2 - 1
        r = r0 + dlr
        c0 = col_regions[0][0] + dlc
        cN = col_regions[-1][0] + dlc
        color = grid[r][c0]  # both ends are same
        for c0_i, c1_i in col_regions:
            out[r][c0_i + dlc] = color
    return out
def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_seps = [i for i in range(h) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_regions = [(row_seps[i]+1, row_seps[i+1]-1) for i in range(len(row_seps)-1)]
    col_regions = [(col_seps[j]+1, col_seps[j+1]-1) for j in range(len(col_seps)-1)]
    out = [row[:] for row in grid]
    for (r0, r1) in row_regions:
        H = r1 - r0 + 1
        dlr = H//2 + (H%2)
        r = r0 + dlr
        W = col_regions[0][1] - col_regions[0][0] + 1
        dlc = W//2 - 1
        c0 = col_regions[0][0] + dlc
        cN = col_regions[-1][0] + dlc
        color = grid[r][c0]
        for (cstart, _) in col_regions:
            out[r][cstart + dlc] = color
    return out