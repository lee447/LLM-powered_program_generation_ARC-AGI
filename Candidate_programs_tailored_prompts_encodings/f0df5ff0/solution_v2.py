from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    if rows == 0:
        return []
    cols = len(grid[0])
    seeds = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
    result = [row.copy() for row in grid]
    for r, c in seeds:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == 0:
                    result[nr][nc] = 1
    return result