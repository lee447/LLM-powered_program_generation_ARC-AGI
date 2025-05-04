from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    five_positions = {(r, c) for r in range(H) for c in range(W) if grid[r][c] == 5}
    rows_with_5 = {r for r, _ in five_positions}
    cols_with_5 = {c for _, c in five_positions}
    result = [row[:] for row in grid]
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0 and v != 5:
                if v == grid[1][1]:
                    if (r, c) != (1, 1):
                        result[r][c] = 0
                else:
                    if r < min(rows_with_5) or c < min(cols_with_5):
                        pass
                    else:
                        pass
    return result