def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # find all nonzero connected components, pick largest
    visited = [[False]*w for _ in range(h)]
    best_comp = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                comp = [(i,j)]
                visited[i][j] = True
                qi = 0
                while qi < len(comp):
                    r,c = comp[qi]; qi+=1
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc] != 0:
                            visited[nr][nc] = True
                            comp.append((nr,nc))
                if len(comp) > len(best_comp):
                    best_comp = comp
    region = set(best_comp)
    rs = [r for r,c in best_comp]; cs = [c for r,c in best_comp]
    minr, maxr = min(rs), max(rs)
    minc, maxc = min(cs), max(cs)
    H = maxr - minr + 1
    W = maxc - minc + 1
    border_color = grid[minr][minc]
    # find exterior clusters
    ext_visited = [[False]*w for _ in range(h)]
    ext_clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and (i,j) not in region and not ext_visited[i][j]:
                comp = [(i,j)]
                ext_visited[i][j] = True
                qi = 0
                while qi < len(comp):
                    r,c = comp[qi]; qi+=1
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not ext_visited[nr][nc] and grid[nr][nc] != 0 and (nr,nc) not in region:
                            ext_visited[nr][nc] = True
                            comp.append((nr,nc))
                ext_clusters.append(comp)
    # find interior islands
    int_visited = [[False]*w for _ in range(h)]
    islands = []
    for r in range(minr+1, maxr):
        for c in range(minc+1, maxc):
            if grid[r][c] != 0 and not int_visited[r][c]:
                col = grid[r][c]
                comp = [(r,c)]
                int_visited[r][c] = True
                qi = 0
                while qi < len(comp):
                    rr,cc = comp[qi]; qi+=1
                    for dr,dc in dirs:
                        nr, nc = rr+dr, cc+dc
                        if minr<nr<maxr and minc<nc<maxc and not int_visited[nr][nc] and grid[nr][nc] == col:
                            int_visited[nr][nc] = True
                            comp.append((nr,nc))
                islands.append((col, comp))
    # build mapping C->D
    mapping = {}
    for comp in ext_clusters:
        cols = {grid[r][c] for r,c in comp}
        if len(cols) == 2:
            for C in list(cols):
                D = (cols - {C}).pop()
                mapping[C] = D
    # build output
    out = [[border_color]*W for _ in range(H)]
    for r in range(minr, maxr+1):
        for c in range(minc, maxc+1):
            if grid[r][c] != 0:
                rr, cc = r - minr, c - minc
                if grid[r][c] in mapping:
                    out[rr][cc] = mapping[grid[r][c]]
                else:
                    out[rr][cc] = grid[r][c]
    return out