def solve(grid):
    H = len(grid)
    W = len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] and not visited[i][j]:
                val = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c,val))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==val:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append(comp)
    mins = sorted({min(r for r,c,_ in comp) for comp in clusters})
    pattern = [0,-1,0,1]
    out = [[0]*W for _ in range(H)]
    for comp in clusters:
        minr = min(r for r,c,_ in comp)
        idx = mins.index(minr)
        shift = pattern[idx%4]
        if idx==0 or idx==len(mins)-1:
            shift = 0
        for r,c,v in comp:
            out[r][c+shift] = v
    return out