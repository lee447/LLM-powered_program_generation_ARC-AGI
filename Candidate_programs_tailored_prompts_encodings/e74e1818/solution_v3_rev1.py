from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [row[:] for row in grid]
    i = 0
    while i < h:
        color_set = {c for c in grid[i] if c != 0}
        if not color_set:
            i += 1
            continue
        rows = [i]
        j = i + 1
        while j < h and {c for c in grid[j] if c != 0} == color_set:
            rows.append(j)
            j += 1
        if len(rows) > 1:
            rev = list(reversed(rows))
            for dest, src in zip(rows, rev):
                out[dest] = grid[src][:]
        i = j
    return out