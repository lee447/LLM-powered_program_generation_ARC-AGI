def solve(grid):
    m, n = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(m-4):
        for c in range(n-4):
            if all(grid[r][c+i]==1 for i in range(5)) and all(grid[r+4][c+i]==1 for i in range(5)) and all(grid[r+i][c]==1 for i in range(5)) and all(grid[r+i][c+4]==1 for i in range(5)):
                anchor = grid[r+2][c+2]
                if anchor not in (0,1):
                    for i in range(1,4):
                        for j in range(1,4):
                            out[r+i][c+j] = anchor
    return out