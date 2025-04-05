from collections import deque
def solve(grid):
    if not grid: 
        return grid
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    dq = deque()
    for r in range(R):
        for c in [0, C-1]:
            if not visited[r][c]:
                dq.append((r,c))
                visited[r][c] = True
    for c in range(C):
        for r in [0, R-1]:
            if not visited[r][c]:
                dq.append((r,c))
                visited[r][c] = True
    while dq:
        r,c = dq.popleft()
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                visited[nr][nc] = True
                dq.append((nr,nc))
    comps = []
    for r in range(R):
        for c in range(C):
            if not visited[r][c]:
                dq = deque([(r,c)])
                visited[r][c] = True
                comp = []
                while dq:
                    rr, cc = dq.popleft()
                    comp.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                            visited[nr][nc] = True
                            dq.append((nr,nc))
                comps.append(comp)
    if not comps:
        return grid
    comp = max(comps, key=len)
    minr = min(r for r,c in comp)
    maxr = max(r for r,c in comp)
    minc = min(c for r,c in comp)
    maxc = max(c for r,c in comp)
    return [grid[r][minc:maxc+1] for r in range(minr, maxr+1)]