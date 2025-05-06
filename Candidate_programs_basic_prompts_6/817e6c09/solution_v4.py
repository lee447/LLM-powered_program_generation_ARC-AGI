def solve(grid):
    h, w = len(grid), len(grid[0])
    is_block = [[False]*w for _ in range(h)]
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==2 and grid[i][j+1]==2 and grid[i+1][j]==2 and grid[i+1][j+1]==2:
                is_block[i][j]=True
    neigh = {}
    for i in range(h-1):
        for j in range(w-1):
            if is_block[i][j]:
                neigh[(i,j)] = []
    for (i,j) in list(neigh):
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di*1, j+dj*1
            if (ni,nj) in neigh:
                neigh[(i,j)].append((ni,nj))
    out = [row[:] for row in grid]
    for (i,j), nbrs in neigh.items():
        if len(nbrs)==1:
            for di in (0,1):
                for dj in (0,1):
                    out[i+di][j+dj] = 8
    return out