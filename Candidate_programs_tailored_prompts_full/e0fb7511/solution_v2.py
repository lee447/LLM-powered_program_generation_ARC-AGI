def solve(grid):
    R = len(grid)
    C = len(grid[0]) if R else 0
    visited = [[False]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                if len(comp) > 1:
                    for x, y in comp:
                        grid[x][y] = 8
    return grid