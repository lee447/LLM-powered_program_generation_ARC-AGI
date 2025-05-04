from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pattern_row = None
    for row in grid:
        if 0 not in row:
            vals = set(row)
            if len(vals) > 1:
                pattern_row = row
                break
    p = next(p for p in range(1, w+1) if all(pattern_row[i] == pattern_row[i+p] for i in range(w-p)))
    pat = pattern_row[:p]
    out = [row[:] for row in grid]
    for i in range(h):
        row = grid[i]
        nonzeros = {x for x in row if x != 0}
        for j in range(w):
            if row[j] == 0:
                if len(nonzeros) == 1:
                    out[i][j] = next(iter(nonzeros))
                else:
                    out[i][j] = pat[j % p]
    return out