from collections import deque, Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] and not visited[r][c]:
                q = deque()
                q.append((r,c))
                cluster = []
                while q:
                    rr, cc = q.popleft()
                    if visited[rr][cc]:
                        continue
                    visited[rr][cc] = True
                    if grid[rr][cc]==0:
                        continue
                    cluster.append((rr,cc))
                    for dr,dc in dirs:
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]:
                            q.append((nr,nc))
                if len(cluster) < 2:
                    continue
                rows = [p[0] for p in cluster]
                cols = [p[1] for p in cluster]
                rmin, rmax = min(rows), max(rows)
                cmin, cmax = min(cols), max(cols)
                col_modes = {}
                colvals = {}
                for rr, cc in cluster:
                    colvals.setdefault(cc, []).append(grid[rr][cc])
                for col in range(cmin, cmax+1):
                    if col in colvals:
                        cnt = Counter(colvals[col])
                        m = min([color for color, num in cnt.items() if num==max(cnt.values())])
                        col_modes[col] = m
                    else:
                        # fill missing column with nearest available mode if possible
                        left = col-1
                        right = col+1
                        fill = 0
                        while left>=cmin or right<=cmax:
                            if left>=cmin and left in col_modes:
                                fill = col_modes[left]
                                break
                            if right<=cmax and right in col_modes:
                                fill = col_modes[right]
                                break
                            left -= 1
                            right += 1
                        col_modes[col] = fill
                for rr in range(rmin, rmax+1):
                    for cc in range(cmin, cmax+1):
                        out[rr][cc] = col_modes[cc]
    return out