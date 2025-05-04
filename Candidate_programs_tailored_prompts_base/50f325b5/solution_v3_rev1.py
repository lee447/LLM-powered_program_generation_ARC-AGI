from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    runs = []
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] == 8:
                start = c
                while c < w and grid[r][c] == 8:
                    c += 1
                runs.append((r, start, c - start))
            else:
                c += 1
    L = max(length for _, _, length in runs) if runs else 0
    starts = {start for r, start, length in runs if length == L}
    for c0 in starts:
        for r in range(h):
            v = grid[r][c0]
            if v == 3:
                grid[r][c0] = 8
            elif v == 8:
                grid[r][c0] = 3
    return grid