from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else 0
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c,color))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                minr = min(r for r,_,_ in cells)
                minc = min(c for _,c,_ in cells)
                comps.append((minr, minc, cells))
    comps.sort(key=lambda x: (x[0], x[1]))
    _, _, target = comps[0]
    minr = min(r for r,_,_ in target)
    maxr = max(r for r,_,_ in target)
    minc = min(c for _,c,_ in target)
    maxc = max(c for _,c,_ in target)
    out_h = maxr - minr + 1
    out_w = maxc - minc + 1
    out = [[0]*out_w for _ in range(out_h)]
    for r,c,v in target:
        out[r-minr][c-minc] = v
    return out