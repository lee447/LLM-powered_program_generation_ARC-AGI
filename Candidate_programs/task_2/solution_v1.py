from collections import deque
def solve(grid):
    rcount, ccount = len(grid), len(grid[0]) if grid else 0
    comp = []
    visited = [[False]*ccount for _ in range(rcount)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(rcount):
        for j in range(ccount):
            if grid[i][j] in (4,9) and not visited[i][j]:
                q = deque()
                q.append((i,j))
                visited[i][j] = True
                cells = []
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<rcount and 0<=nc<ccount and not visited[nr][nc] and grid[nr][nc] in (4,9):
                            visited[nr][nc] = True
                            q.append((nr,nc))
                comp.append(cells)
    if not comp:
        return grid
    best = max(comp, key=len)
    rmin = min(r for r,c in best)
    rmax = max(r for r,c in best)
    cmin = min(c for r,c in best)
    cmax = max(c for r,c in best)
    out = [ row[cmin:cmax+1] for row in grid[rmin:rmax+1] ]
    return out