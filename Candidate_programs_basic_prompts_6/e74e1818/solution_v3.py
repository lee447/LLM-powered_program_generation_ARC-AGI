from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and not visited[i][j]:
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                min_i = min(x for x,_ in comp)
                max_i = max(x for x,_ in comp)
                min_j = min(y for _,y in comp)
                max_j = max(y for _,y in comp)
                for x,y in comp:
                    rx = min_i + max_i - x
                    ry = min_j + max_j - y
                    out[rx][ry] = c
    return out