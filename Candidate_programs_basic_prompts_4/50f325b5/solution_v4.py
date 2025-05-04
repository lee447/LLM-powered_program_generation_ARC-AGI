from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    pts = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 8]
    minr = min(i for i, _ in pts)
    maxr = max(i for i, _ in pts)
    minc = min(j for _, j in pts)
    maxc = max(j for _, j in pts)
    Ah, Aw = maxr - minr + 1, maxc - minc + 1
    Arel = {(i - minr, j - minc) for i, j in pts}
    Bh, Bw = Aw, Ah
    Brel = {(Aw - 1 - c, r) for r, c in Arel}
    res = [row[:] for row in grid]
    target = 3
    seen = [[False]*m for _ in range(n)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target and not seen[i][j]:
                comp = [(i,j)]
                seen[i][j] = True
                q = [(i,j)]
                for x,y in q:
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not seen[nx][ny] and grid[nx][ny] == target:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                h = max(rs)-min(rs)+1
                w = max(cs)-min(cs)+1
                if h == Bh and w == Bw:
                    br, bc = min(rs), min(cs)
                    for dr, dc in Brel:
                        res[br+dr][bc+dc] = 8
    return res