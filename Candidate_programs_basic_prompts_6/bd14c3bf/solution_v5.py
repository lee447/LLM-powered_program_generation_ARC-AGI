def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                # flood-fill to get component
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==1:
                            seen[nr][nc]=True
                            stack.append((nr,nc))
                # bounding box
                minr = min(r for r,c in comp)
                maxr = max(r for r,c in comp)
                minc = min(c for r,c in comp)
                maxc = max(c for r,c in comp)
                if maxr-minr>=2 and maxc-minc>=2:
                    # interior zeros?
                    ok = True
                    for rr in range(minr+1, maxr):
                        for cc in range(minc+1, maxc):
                            if grid[rr][cc]!=0:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        continue
                    # comp cells on perimeter?
                    for r,c in comp:
                        if not (r==minr or r==maxr or c==minc or c==maxc):
                            ok = False
                            break
                    if not ok:
                        continue
                    # recolor entire comp
                    for r,c in comp:
                        out[r][c] = 2
    return out