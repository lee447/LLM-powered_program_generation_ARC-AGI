def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                comp = [(i,j)]
                visited[i][j] = True
                q = [(i,j)]
                while q:
                    r,c = q.pop()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            comp.append((nr,nc))
                if len(comp) >= 4:
                    rs = [r for r,c in comp]
                    cs = [c for r,c in comp]
                    r0, r1 = min(rs), max(rs)
                    c0, c1 = min(cs), max(cs)
                    clusters.append((r0, r1, c0, c1, comp))
    groups = {}
    for r0, r1, c0, c1, comp in clusters:
        h = r1 - r0 + 1
        w = c1 - c0 + 1
        groups.setdefault((h,w), []).append((r0, c0))
    res = [[0]*W for _ in range(H)]
    for (h,w), boxes in groups.items():
        if h == w:
            r0, c0 = boxes[0]
            template = [ [grid[r0+i][c0+j] for j in range(w)] for i in range(h) ]
        else:
            # column-mode template
            colm = []
            for dj in range(w):
                cnt = {}
                for r0, c0 in boxes:
                    v = grid[r0][c0+dj]
                    if v:
                        cnt[v] = cnt.get(v,0) + 1
                if cnt:
                    colm.append(max(cnt.items(), key=lambda x:(x[1],x[0]))[0])
                else:
                    colm.append(0)
            template = [colm[:] for _ in range(h)]
        for r0, c0 in boxes:
            for i in range(h):
                for j in range(w):
                    res[r0+i][c0+j] = template[i][j]
    return res