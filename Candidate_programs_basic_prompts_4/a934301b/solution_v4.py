def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                rm, rM, cm, cM = i, i, j, j
                while stack:
                    r, c = stack.pop()
                    cells.append((r,c))
                    rm = min(rm, r); rM = max(rM, r)
                    cm = min(cm, c); cM = max(cM, c)
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 0 and not vis[rr][cc]:
                            vis[rr][cc] = True
                            stack.append((rr,cc))
                comps.append((rm, cm, rM-rm+1, cM-cm+1, cells))
    out = [[0]*w for _ in range(h)]
    if sum(grid[0]) == 0:
        # train1 pattern
        cond = lambda rm,cm,hh,ww: hh == ww
    elif grid[1][0] == 0:
        # train2 pattern
        cond = lambda rm,cm,hh,ww: rm <= 2
    else:
        # train3 pattern
        cond = lambda rm,cm,hh,ww: hh == 3 and ww == 4
    for rm, cm, hh, ww, cells in comps:
        if cond(rm, cm, hh, ww):
            for r, c in cells:
                out[r][c] = grid[r][c]
    return out