def solve(grid):
    H = len(grid)
    W = len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                if len(comp) >= 2:
                    for x, y in comp:
                        res[x][y] = 8
    return res