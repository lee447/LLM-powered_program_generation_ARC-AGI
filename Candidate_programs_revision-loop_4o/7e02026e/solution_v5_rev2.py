def solve(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def flood_fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 0 or visited[r][c]:
            return
        visited[r][c] = True
        grid[r][c] = 3
        flood_fill(r + 1, c)
        flood_fill(r - 1, c)
        flood_fill(r, c + 1)
        flood_fill(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 8:
                if (c > 0 and grid[r][c-1] == 0) or (c < cols-1 and grid[r][c+1] == 0) or (r > 0 and grid[r-1][c] == 0) or (r < rows-1 and grid[r+1][c] == 0):
                    flood_fill(r, c)
    
    return grid