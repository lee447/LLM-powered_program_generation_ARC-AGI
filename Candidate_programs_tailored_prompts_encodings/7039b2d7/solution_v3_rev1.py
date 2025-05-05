from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    hr = [r for r in range(h) if len(set(grid[r])) == 1]
    hc = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1]
    hr.sort()
    hc.sort()
    row_bounds = [-1] + hr + [h]
    col_bounds = [-1] + hc + [w]
    row_segs = [(row_bounds[i] + 1, row_bounds[i+1] - 1) for i in range(len(row_bounds) - 1) if row_bounds[i] + 1 <= row_bounds[i+1] - 1]
    col_segs = [(col_bounds[i] + 1, col_bounds[i+1] - 1) for i in range(len(col_bounds) - 1) if col_bounds[i] + 1 <= col_bounds[i+1] - 1]
    result = []
    for rs, _ in row_segs:
        row = []
        for cs, _ in col_segs:
            row.append(grid[rs][cs])
        result.append(row)
    return result