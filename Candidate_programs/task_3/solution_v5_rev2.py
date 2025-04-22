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
                has_marker = any(grid[r][c] > 1 for r,c in comp)
                if not has_marker:
                    continue
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                comp_set = set(comp)
                for r,c in comp:
                    color = grid[r][c]
                    if color <= 1:
                        continue
                    r0 = minr + maxr - r
                    c0 = minc + maxc - c
                    pts = {(r,c), (r0,c0), (r0,c), (r,c0)}
                    for x,y in pts & comp_set:
                        if out[x][y] == 1:
                            out[x][y] = color
    return out