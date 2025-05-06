from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    visited = [[False]*w for _ in range(h)]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                count8 = 0
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    if grid[x][y] == 8:
                        count8 += 1
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                if count8 > 1:
                    for x,y in comp:
                        res[x][y] = 0
    return res