def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    regions = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs4:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                regions.append(comp)
    if not regions:
        return grid
    M = set(max(regions, key=len))
    nonM = [(i,j) for i in range(H) for j in range(W) if (i,j) not in M]
    out = [row[:] for row in grid]
    for i,j in nonM:
        if i==0 or i==H-1 or j==0 or j==W-1:
            continue
        for di in (-1,0,1):
            for dj in (-1,0,1):
                if di==0 and dj==0: continue
                ni, nj = i+di, j+dj
                if (ni,nj) in M:
                    out[i][j] = 2
                    di = dj = None
                    break
            else:
                continue
            break
    for i,j in M:
        mind = H+W
        for ni,nj in nonM:
            d = max(abs(i-ni), abs(j-nj))
            if d < mind:
                mind = d
            if mind==1:
                break
        if mind==1:
            out[i][j] = 8
        elif mind==2:
            out[i][j] = 6
    return out