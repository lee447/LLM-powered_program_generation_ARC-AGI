def solve(grid):
    H=len(grid)
    W=len(grid[0])
    rowsZ=[r for r in range(H) if any(grid[r][c]==0 for c in range(W))]
    best_path=[]
    best_len=0
    best_last=-1
    best_startc=-1
    for r0 in rowsZ:
        for c0 in range(W):
            if grid[r0][c0]==0:
                for delta in (1,-1):
                    path=[(r0,c0)]
                    c=c0
                    r=r0
                    while True:
                        nr=r+1
                        nc=c+delta
                        if nr<0 or nr>=H or nc<0 or nc>=W: break
                        if grid[nr][nc]==0:
                            path.append((nr,nc))
                            r=nr; c=nc
                        else:
                            break
                    ln=len(path)
                    last=path[-1][0]
                    if ln>best_len or (ln==best_len and last>best_last) or (ln==best_len and last==best_last and c0>best_startc):
                        best_path=path
                        best_len=ln
                        best_last=last
                        best_startc=c0
    res=[row[:] for row in grid]
    for r,c in best_path:
        res[r][c]=8
    return res