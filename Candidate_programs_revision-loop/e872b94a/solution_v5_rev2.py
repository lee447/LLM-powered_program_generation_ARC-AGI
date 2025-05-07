from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    clusters = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                clusters += 1
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    return [[0] for _ in range(clusters + 1)]