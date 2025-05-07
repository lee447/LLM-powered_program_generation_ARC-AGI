from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zeros = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 0]
    diag1 = [r - c for r, c in zeros]
    diag2 = [r + c for r, c in zeros]
    if max(diag1) - min(diag1) <= max(diag2) - min(diag2):
        D = sorted(diag1)[len(diag1) // 2]
        out = [row[:] for row in grid]
        for r, c in zeros:
            if r - c == D:
                out[r][c] = 8
    else:
        D = sorted(diag2)[len(diag2) // 2]
        out = [row[:] for row in grid]
        for r, c in zeros:
            if r + c == D:
                out[r][c] = 8
    return out