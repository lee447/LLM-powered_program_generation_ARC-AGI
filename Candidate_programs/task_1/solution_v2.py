from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not visited[i][j]:
                comp = []
                dq = deque()
                dq.append((i,j))
                visited[i][j] = True
                while dq:
                    r,c = dq.popleft()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w:
                            if grid[nr][nc] and not visited[nr][nc]:
                                visited[nr][nc] = True
                                dq.append((nr,nc))
                # Remove border rows (top and bottom of whole grid)
                sub = [(r,c) for (r,c) in comp if r not in (0, h-1)]
                if len(sub) < 2:
                    continue
                rmin = min(r for (r,c) in sub)
                rmax = max(r for (r,c) in sub)
                cmin = min(c for (r,c) in sub)
                cmax = max(c for (r,c) in sub)
                freq = {}
                for (r,c) in sub:
                    freq[grid[r][c]] = freq.get(grid[r][c],0)+1
                mode = max(freq, key=lambda k: freq[k])
                for r in range(rmin, rmax+1):
                    for c in range(cmin, cmax+1):
                        out[r][c] = mode
    return out