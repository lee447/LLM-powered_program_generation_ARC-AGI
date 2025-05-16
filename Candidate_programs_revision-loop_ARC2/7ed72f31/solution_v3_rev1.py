def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==color:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append((color, comp))
    pivots = [comp for color,comp in clusters if color==2]
    out = [row[:] for row in grid]
    for color, comp in clusters:
        if color==bg or color==2:
            continue
        found = None
        for p in pivots:
            pr0 = [r for r,_ in p]
            pc0 = [c for _,c in p]
            rmin,rmax = min(pr0), max(pr0)
            cmin,cmax = min(pc0), max(pc0)
            size = len(p)
            for r,c in comp:
                for pr,pc in p:
                    if size==1:
                        if max(abs(r-pr),abs(c-pc))==1:
                            found = (pr,pc,'rot')
                            break
                    else:
                        if abs(r-pr)+abs(c-pc)==1:
                            if rmin==rmax:
                                found = (rmin,pc,'vert')
                            else:
                                found = (pr,cmin,'horiz')
                            break
                if found: break
            if found: break
        if not found: continue
        pr,pc,mode = found
        for r,c in comp:
            if mode=='rot':
                nr, nc = 2*pr-r, 2*pc-c
            elif mode=='horiz':
                nr, nc = r, pc - (c-pc)
            else:
                nr, nc = pr - (r-pr), c
            if 0<=nr<h and 0<=nc<w and out[nr][nc]==bg:
                out[nr][nc] = color
    return out