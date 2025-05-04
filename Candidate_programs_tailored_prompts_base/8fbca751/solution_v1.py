def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(r,c):
        stack=[(r,c)]
        comp=set()
        visited[r][c]=True
        while stack:
            x,y = stack.pop()
            comp.add((x,y))
            for dx,dy in dirs:
                nx,ny = x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==8:
                    visited[nx][ny]=True
                    stack.append((nx,ny))
        return comp
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not visited[i][j]:
                comps.append(flood(i,j))
    orth_pairs = [((1,0),(0,1)),((1,0),(0,-1)),((-1,0),(0,1)),((-1,0),(0,-1))]
    for comp in comps:
        for (r,c) in comp:
            for (d1,d2) in orth_pairs:
                r1,c1 = r+d1[0], c+d1[1]
                r2,c2 = r+d2[0], c+d2[1]
                rd,cd = r+d1[0]+d2[0], c+d1[1]+d2[1]
                if (r1,c1) in comp and (r2,c2) in comp and (rd,cd) not in comp:
                    dr, dc = d1[0]+d2[0], d1[1]+d2[1]
                    sdr = 1 if dr>0 else (-1 if dr<0 else 0)
                    sdc = 1 if dc>0 else (-1 if dc<0 else 0)
                    for i in (0,1):
                        for j in (0,1):
                            rr = rd + i*sdr
                            cc = cd + j*sdc
                            if 0<=rr<h and 0<=cc<w and out[rr][cc]==0:
                                out[rr][cc]=2
    return out