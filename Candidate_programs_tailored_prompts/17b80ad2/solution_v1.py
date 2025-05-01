from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    stripe_cols = [c for c in range(w) if grid[h-1][c] != 0]
    for c in stripe_cols:
        anchors = [(r, grid[r][c]) for r in range(h) if grid[r][c] != 0]
        anchors.sort()
        seq = []
        last_val = None
        for r, v in anchors:
            if v != last_val:
                seq.append(v)
                last_val = v
        last_rows = []
        for color in seq:
            for r, v in reversed(anchors):
                if v == color:
                    last_rows.append(r)
                    break
        start = 0
        for v, end in zip(seq, last_rows):
            for r in range(start, end+1):
                out[r][c] = v
            start = end + 1
        if start < h:
            fill_val = seq[-1]
            for r in range(start, h):
                out[r][c] = fill_val
    return out