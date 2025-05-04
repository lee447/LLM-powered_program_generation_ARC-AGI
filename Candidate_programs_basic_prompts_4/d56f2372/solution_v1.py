def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c>0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r,c0 = stack.pop()
                    cells.append((r,c0))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c0+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==grid[i][j]:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                minr = min(r for r,_ in cells)
                maxr = max(r for r,_ in cells)
                minc = min(c0 for _,c0 in cells)
                maxc = max(c0 for _,c0 in cells)
                max_run = 0
                for r in range(minr, maxr+1):
                    run = 0
                    for c0 in range(minc, maxc+1):
                        if grid[r][c0]==grid[i][j]:
                            run += 1
                            if run>max_run: max_run = run
                        else:
                            run = 0
                comps.append((grid[i][j], len(cells), minr, maxr, minc, maxc, max_run))
    candidates = [p for p in comps if p[6]==3]
    if not candidates:
        candidates = comps
    col, size, r0, r1, c0, c1, _ = max(candidates, key=lambda x: x[1])
    out = []
    for r in range(r0, r1+1):
        row = []
        for c in range(c0, c1+1):
            row.append(col if grid[r][c]==col else 0)
        out.append(row)
    return out