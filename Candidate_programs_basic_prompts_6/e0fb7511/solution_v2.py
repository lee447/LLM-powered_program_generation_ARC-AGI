from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    result = [row.copy() for row in grid]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                if len(comp) > 1:
                    for x, y in comp:
                        result[x][y] = 8
    return result