def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                h = max(rs) - min(rs) + 1
                comps.append((col, cells, len(cells), h))
    out = [[0]*W for _ in range(H)]
    for col, cells, size, h in comps:
        if size >= 4 and h > 1:
            for r, c in cells:
                out[r][c] = col
    return out