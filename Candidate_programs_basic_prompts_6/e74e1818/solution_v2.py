def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    visited = [[False]*cols for _ in range(rows)]
    out = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                min_r = min(r for r, _ in comp)
                max_r = max(r for r, _ in comp)
                for r, c in comp:
                    out[min_r + max_r - r][c] = color
    return out