from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    
    def flood_fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or result[r][c] != 8:
            return
        result[r][c] = 2
        flood_fill(r - 1, c)
        flood_fill(r + 1, c)
        flood_fill(r, c - 1)
        flood_fill(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                flood_fill(r, c)

    return result