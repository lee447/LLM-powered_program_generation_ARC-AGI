def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and (i, j) not in visited:
                stack = [(i, j)]
                visited.add((i, j))
                coords = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 8 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
                            coords.append((nx, ny))
                rs = [r for r, _ in coords]
                cs = [c for _, c in coords]
                rmin, rmax = min(rs), max(rs)
                cmin, cmax = min(cs), max(cs)
                for r in range(rmin, rmax + 1):
                    for c in range(cmin, cmax + 1):
                        if grid[r][c] == 0:
                            grid[r][c] = 2
    return grid