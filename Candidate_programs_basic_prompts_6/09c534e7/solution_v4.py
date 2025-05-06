def solve(grid):
    h = len(grid)
    w = len(grid[0])
    q = [(i, j, grid[i][j]) for i in range(h) for j in range(w) if grid[i][j] > 1]
    while q:
        newq = []
        for i, j, c in q:
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 0:
                    grid[ni][nj] = c
                    newq.append((ni, nj, c))
        q = newq
    return grid