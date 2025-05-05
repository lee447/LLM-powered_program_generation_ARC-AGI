from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    rects = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                minr = maxr = i
                minc = maxc = j
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    if r < minr: minr = r
                    if r > maxr: maxr = r
                    if c < minc: minc = c
                    if c > maxc: maxc = c
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 8:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                rects.append((minr, maxr, minc, maxc))
    out = [[0]*w for _ in range(h)]
    for minr, maxr, minc, maxc in rects:
        for r in range(minr, maxr+1):
            for c in range(minc, maxc+1):
                out[r][c] = grid[r][c]
    return out