def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    m = len(grid[0]) if n>0 else 0
    result = [row[:] for row in grid]
    blues = sorted((i,j) for i in range(n) for j in range(m) if grid[i][j]==1)
    if len(blues)<2:
        return result
    step = blues[1][0]-blues[0][0]
    last_r, last_c = blues[-1]
    r, c = last_r+step, last_c+step
    while 0<=r<n and 0<=c<m:
        result[r][c] = 2
        r += step
        c += step
    return result