from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_subgrid(grid):
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 3:
                    return i, j
        return None, None

    def extract_subgrid(grid, start_row, start_col):
        subgrid = []
        for i in range(start_row, len(grid)):
            if grid[i][start_col] != 3:
                break
            row = []
            for j in range(start_col, len(grid[0])):
                if grid[i][j] == 3:
                    row.append(grid[i][j])
                else:
                    break
            subgrid.append(row)
        return subgrid

    def find_non_three_subgrid(grid, start_row, start_col):
        subgrid = []
        for i in range(start_row, len(grid)):
            if grid[i][start_col] == 3:
                continue
            row = []
            for j in range(start_col, len(grid[0])):
                if grid[i][j] != 3:
                    row.append(grid[i][j])
                else:
                    break
            if row:
                subgrid.append(row)
        return subgrid

    start_row, start_col = find_subgrid(grid)
    if start_row is None or start_col is None:
        return []

    subgrid = find_non_three_subgrid(grid, start_row, start_col)
    if not subgrid:
        return []

    min_col = min(len(row) for row in subgrid)
    return [row[:min_col] for row in subgrid]