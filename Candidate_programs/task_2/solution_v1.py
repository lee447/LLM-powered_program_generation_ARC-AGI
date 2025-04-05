from collections import deque
def solve(grid):
    R = len(grid)
    if R == 0:
        return grid
    C = len(grid[0])
    S = {4,6,7,9}
    visited = [[False]*C for _ in range(R)]
    comps = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] in S and not visited[r][c]:
                dq = deque([(r,c)])
                visited[r][c] = True
                comp = []
                while dq:
                    rr, cc = dq.popleft()
                    comp.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc] in S:
                            visited[nr][nc] = True
                            dq.append((nr,nc))
                comps.append(comp)
    if not comps:
        return grid
    comp = max(comps, key=lambda comp: len(comp))
    minr = min(r for r,c in comp)
    maxr = max(r for r,c in comp)
    minc = min(c for r,c in comp)
    maxc = max(c for r,c in comp)
    return [row[minc:maxc+1] for row in grid[minr:maxr+1]]