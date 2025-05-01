def solve(grid):
    h, w = len(grid), len(grid[0])
    init = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if init[i][j] != 0 and not visited[i][j]:
                q = [(i,j)]
                visited[i][j] = True
                cells = [(i,j)]
                for r,c in q:
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and init[nr][nc] != 0:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            cells.append((nr,nc))
                minR = min(r for r,c in cells)
                maxR = max(r for r,c in cells)
                minC = min(c for r,c in cells)
                maxC = max(c for r,c in cells)
                comps.append((set(cells), minR, maxR, minC, maxC, maxR-minR+1))
    seeds = [(r,c,init[r][c]) for r in range(h) for c in range(w) if init[r][c] not in (0,1)]
    for sr,sc,sv in seeds:
        seed_comp = None
        for cells,minR,maxR,minC,maxC,hh in comps:
            if minR<=sr<=maxR and minC<=sc<=maxC and (sr,sc) in cells:
                seed_comp = (cells,minR,maxR,minC,maxC,hh)
                break
        if seed_comp is None: continue
        scells, sminR,smaxR,sminC,smaxC,sh = seed_comp
        for cells,minR,maxR,minC,maxC,hh in comps:
            if (cells,minR,maxR,minC,maxC,hh) is seed_comp or (minR<=sr<=maxR and hh<sh):
                for r in range(minR+1, maxR):
                    for c in range(minC+1, maxC):
                        if init[r][c] == 1:
                            grid[r][c] = sv
    return grid