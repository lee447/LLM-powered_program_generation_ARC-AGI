def solve(grid):
    from collections import deque, Counter
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    used = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] and not used[r][c]:
                q = deque()
                q.append((r,c))
                cluster = []
                while q:
                    rr, cc = q.popleft()
                    if used[rr][cc]:
                        continue
                    if grid[rr][cc] == 0:
                        continue
                    used[rr][cc] = True
                    cluster.append((rr,cc))
                    for dr,dc in dirs:
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<h and 0<=nc<w and not used[nr][nc] and grid[nr][nc]:
                            q.append((nr,nc))
                if len(cluster) < 2:
                    continue
                colvals = {}
                for rr, cc in cluster:
                    colvals.setdefault(cc, []).append(grid[rr][cc])
                col_modes = {}
                for col in colvals:
                    cnt = Counter(colvals[col])
                    m = min(k for k,v in cnt.items() if v==max(cnt.values()))
                    col_modes[col] = m
                for rr, cc in cluster:
                    out[rr][cc] = col_modes[cc]
    return out