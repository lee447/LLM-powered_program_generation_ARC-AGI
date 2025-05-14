def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                # Fill horizontally to the right
                for cc in range(c + 1, cols):
                    if grid[r][cc] == 0:
                        output[r][cc] = 2
                    else:
                        break
                # Fill vertically downwards
                for rr in range(r + 1, rows):
                    if grid[rr][c] == 0:
                        output[rr][c] = 2
                    else:
                        break
    return output