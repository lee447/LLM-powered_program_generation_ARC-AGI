def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque, defaultdict
    # find the anchor L-shape (value 2) component
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    L = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                # BFS to get the full 2-component
                q = deque([(i,j)])
                visited[i][j] = True
                L.append((i,j))
                while q:
                    r,c = q.popleft()
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 2:
                            visited[nr][nc] = True
                            L.append((nr,nc))
                            q.append((nr,nc))
                break
        if L: break
    # row->cols and col->rows for L
    rows = defaultdict(list)
    cols = defaultdict(list)
    for r,c in L:
        rows[r].append(c)
        cols[c].append(r)
    # detect horizontal arm: contiguous run length>=2, choose max row
    anchor_row = max(r for r,cs in rows.items() if any(cs[k+1]-cs[k]==1 for k in range(len(cs)-1)))
    # detect vertical arm: contiguous run in col, unique
    anchor_col = next(c for c,rs in cols.items() if any(rs[k+1]-rs[k]==1 for k in range(len(rs)-1)))
    # find all red (1) clusters
    visited1 = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited1[i][j]:
                q = deque([(i,j)])
                visited1[i][j] = True
                cells = [(i,j)]
                minr, maxr, minc, maxc = i, i, j, j
                while q:
                    r,c = q.popleft()
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited1[nr][nc] and grid[nr][nc] == 1:
                            visited1[nr][nc] = True
                            cells.append((nr,nc))
                            q.append((nr,nc))
                            minr = min(minr,nr); maxr = max(maxr,nr)
                            minc = min(minc,nc); maxc = max(maxc,nc)
                cy = (minr+maxr)/2
                cx = (minc+maxc)/2
                clusters.append((cells, minr, maxr, minc, maxc, cy, cx))
    # find cluster under horizontal arm
    H = [c for c in clusters if c[1] <= anchor_row <= c[2] and c[5] > anchor_row]
    if H:
        hor = min(H, key=lambda c: c[5])
        for r,c in hor[0]:
            grid[r][c] = 2
    # find cluster under vertical arm
    V = [c for c in clusters if c[3] <= anchor_col <= c[4] and c[6] > anchor_col]
    if V:
        ver = min(V, key=lambda c: c[6])
        for r,c in ver[0]:
            grid[r][c] = 2
    return grid