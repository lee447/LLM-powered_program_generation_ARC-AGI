from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and g[i][j] == 0:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and g[nx][ny] == 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                if len(comp) > 1:
                    for x, y in comp:
                        g[x][y] = 8
    return g