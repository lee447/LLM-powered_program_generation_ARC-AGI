from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    cols = [c for c in range(w) if out[0][c] == 1]
    if cols:
        start, end = min(cols), max(cols)
        size = len(cols)
        for r in range(size):
            for c in range(start, end + 1):
                if out[r][c] == 1:
                    out[r][c] = 0
        return out
    cols = [c for c in range(w) if out[h-1][c] == 1]
    if cols:
        start, end = min(cols), max(cols)
        size = len(cols)
        for r in range(h-size, h):
            for c in range(start, end + 1):
                if out[r][c] == 1:
                    out[r][c] = 0
        return out
    rows = [r for r in range(h) if out[r][0] == 1]
    if rows:
        start, end = min(rows), max(rows)
        size = len(rows)
        for c in range(size):
            for r in range(start, end + 1):
                if out[r][c] == 1:
                    out[r][c] = 0
        return out
    rows = [r for r in range(h) if out[r][w-1] == 1]
    if rows:
        start, end = min(rows), max(rows)
        size = len(rows)
        for c in range(w-size, w):
            for r in range(start, end + 1):
                if out[r][c] == 1:
                    out[r][c] = 0
    return out