from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comp_set = set(comp)
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                seen = set()
                for r,c in comp:
                    if (r,c) in seen:
                        continue
                    r0 = minr+maxr-r
                    c0 = minc+maxc-c
                    orbit = {(r,c)}
                    for rr,cc in [(r0,c),(r,c0),(r0,c0)]:
                        if (rr,cc) in comp_set:
                            orbit.add((rr,cc))
                    seen |= orbit
                    colors = [grid[x][y] for x,y in orbit if grid[x][y] > 1]
                    if not colors:
                        continue
                    color = colors[0]
                    for x,y in orbit:
                        if out[x][y] == 1:
                            out[x][y] = color
    return out