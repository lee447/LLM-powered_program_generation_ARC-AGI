from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not visited[y][x]:
                col = grid[y][x]
                stack = [(y, x)]
                comp = []
                visited[y][x] = True
                while stack:
                    cy, cx = stack.pop()
                    comp.append((cy, cx))
                    for dy, dx in dirs:
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == col:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                miny = min(p[0] for p in comp); maxy = max(p[0] for p in comp)
                minx = min(p[1] for p in comp); maxx = max(p[1] for p in comp)
                sub = [grid[i][minx:maxx+1] for i in range(miny, maxy+1)]
                bh, bw = len(sub), len(sub[0])
                sym = True
                for i in range(bh):
                    for j in range(bw):
                        if sub[i][j] != sub[i][bw-1-j]:
                            sym = False
                            break
                    if not sym:
                        break
                if sym:
                    return sub
    return []