from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    anchors = {(r, c) for r in range(h) for c in range(w) if grid[r][c] in (1, 8)}
    res = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 8:
                if 0 <= c - 1 and c + 1 < w and grid[r][c - 1] == 0 and grid[r][c + 1] == 0:
                    if (r, c - 1) not in anchors and (r, c + 1) not in anchors:
                        res[r][c - 1] = 4
                        res[r][c + 1] = 4
                if 0 <= r - 1 and r + 1 < h and grid[r - 1][c] == 0 and grid[r + 1][c] == 0:
                    if (r - 1, c) not in anchors and (r + 1, c) not in anchors:
                        res[r - 1][c] = 4
                        res[r + 1][c] = 4
    for r in range(h - 2):
        for c in range(w - 2):
            if grid[r][c] == 1 and grid[r + 1][c + 1] == 8 and grid[r + 2][c + 2] == 1:
                if grid[r + 1][c] == 0 and (r + 1, c) not in anchors:
                    res[r + 1][c] = 4
                if grid[r + 1][c + 2] == 0 and (r + 1, c + 2) not in anchors:
                    res[r + 1][c + 2] = 4
                if grid[r][c + 1] == 0 and (r, c + 1) not in anchors:
                    res[r][c + 1] = 4
                if grid[r + 2][c + 1] == 0 and (r + 2, c + 1) not in anchors:
                    res[r + 2][c + 1] = 4
    for r in range(h - 2):
        for c in range(2, w):
            if grid[r][c] == 1 and grid[r + 1][c - 1] == 8 and grid[r + 2][c - 2] == 1:
                if grid[r + 1][c] == 0 and (r + 1, c) not in anchors:
                    res[r + 1][c] = 4
                if grid[r + 1][c - 2] == 0 and (r + 1, c - 2) not in anchors:
                    res[r + 1][c - 2] = 4
                if grid[r][c - 1] == 0 and (r, c - 1) not in anchors:
                    res[r][c - 1] = 4
                if grid[r + 2][c - 1] == 0 and (r + 2, c - 1) not in anchors:
                    res[r + 2][c - 1] = 4
    return res