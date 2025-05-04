from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    visited = [[False] * w for _ in range(h)]
    clusters = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not visited[i][j]:
                clusters += 1
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 5:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
    return [[0] for _ in range(clusters + 1)]