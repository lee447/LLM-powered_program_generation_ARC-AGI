def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    blocks = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] != bg:
                c = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                coords = []
                while stack:
                    x, y = stack.pop()
                    coords.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                mr = min(r for r,_ in coords)
                blocks.append((mr, coords, c))
    blocks.sort(key=lambda x: x[0])
    new = [row[:] for row in grid]
    for _, coords, _ in blocks:
        for r, c in coords:
            new[r][c] = bg
    for idx, (_, coords, c) in enumerate(blocks):
        d = -1 if idx % 2 == 0 else 1
        for r, cc in coords:
            new[r][cc + d] = c
    return new