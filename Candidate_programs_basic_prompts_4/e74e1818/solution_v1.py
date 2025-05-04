from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                cells = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                rmin = min(r for r, _ in cells)
                rmax = max(r for r, _ in cells)
                for r, c in cells:
                    nr = rmin + rmax - r
                    out[nr][c] = col
    return out