from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                marker = None
                while stack:
                    x, y = stack.pop()
                    comp.append((x,y))
                    if grid[x][y] > 1:
                        marker = grid[x][y]
                    for dx, dy in dirs4:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                if marker is None:
                    continue
                for x, y in comp:
                    if grid[x][y] == 1:
                        interior = True
                        for dx, dy in dirs8:
                            nx, ny = x+dx, y+dy
                            if not (0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0):
                                interior = False
                                break
                        if interior:
                            out[x][y] = marker
    return out