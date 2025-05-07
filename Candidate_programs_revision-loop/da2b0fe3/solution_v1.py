from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    coords = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0 and grid[r][c] != 3]
    if not coords:
        return grid
    minr = min(r for r, _ in coords)
    maxr = max(r for r, _ in coords)
    minc = min(c for _, c in coords)
    maxc = max(c for _, c in coords)
    max_row_count = -1
    row_idx = minr
    for r in range(minr, maxr+1):
        count = 0
        local_max = 0
        for c in range(minc, maxc+1):
            if grid[r][c] == 0:
                count += 1
                if count > local_max:
                    local_max = count
            else:
                count = 0
        if local_max > max_row_count:
            max_row_count = local_max
            row_idx = r
    max_col_count = -1
    col_idx = minc
    for c in range(minc, maxc+1):
        count = 0
        local_max = 0
        for r in range(minr, maxr+1):
            if grid[r][c] == 0:
                count += 1
                if count > local_max:
                    local_max = count
            else:
                count = 0
        if local_max > max_col_count:
            max_col_count = local_max
            col_idx = c
    if max_row_count >= max_col_count:
        for c in range(C):
            grid[row_idx][c] = 3
    else:
        for r in range(R):
            grid[r][col_idx] = 3
    return grid