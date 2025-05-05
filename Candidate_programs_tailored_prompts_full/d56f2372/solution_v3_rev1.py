from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                minr = min(r for r,c in comp)
                maxr = max(r for r,c in comp)
                minc = min(c for r,c in comp)
                maxc = max(c for r,c in comp)
                dh = maxr - minr + 1
                dw = maxc - minc + 1
                sub = [[0]*dw for _ in range(dh)]
                for r, c in comp:
                    sub[r-minr][c-minc] = color
                sym = True
                for rr in range(dh):
                    for cc in range(dw):
                        if sub[rr][cc] != sub[rr][dw-1-cc]:
                            sym = False
                            break
                    if not sym:
                        break
                if sym:
                    return sub
    return grid