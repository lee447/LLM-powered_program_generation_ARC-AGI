from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 8:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                            cells.append((nx,ny))
                minr = min(r for r,c in cells)
                maxr = max(r for r,c in cells)
                minc = min(c for r,c in cells)
                maxc = max(c for r,c in cells)
                for r in range(minr, maxr+1):
                    for c in range(minc, maxc+1):
                        if grid[r][c] == 0:
                            grid[r][c] = 2
    return grid