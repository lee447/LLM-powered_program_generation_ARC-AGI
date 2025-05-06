from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=lambda k: freq[k])
    visited = [[False]*n for _ in range(m)]
    shapes = []
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j] != bg:
                c = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                coords = []
                min_row = i
                while stack:
                    x, y = stack.pop()
                    coords.append((x, y))
                    if x < min_row:
                        min_row = x
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                shapes.append((min_row, coords, c))
    shapes.sort(key=lambda x: x[0])
    res = [row[:] for row in grid]
    for idx, (_, coords, c) in enumerate(shapes):
        off = -1 if idx % 2 == 0 else 1
        for x, y in coords:
            res[x][y] = bg
        for x, y in coords:
            res[x][y + off] = c
    return res