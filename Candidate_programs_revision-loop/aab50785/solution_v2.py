def solve(grid):
    h, w = len(grid), len(grid[0])
    windows = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==8 and grid[r][c+1]==8 and grid[r+1][c]==8 and grid[r+1][c+1]==8:
                windows.append((r,c))
    out = []
    for r,c in windows:
        row = []
        for dr,dc in [( -2,0),(-1,1),(0,2),(1,3),(2,4)]:
            rr, cc = r+dr, c+dc
            if 0<=rr<h and 0<=cc<w:
                row.append(grid[rr][cc])
            else:
                row.append(0)
        out.append(row)
    return out