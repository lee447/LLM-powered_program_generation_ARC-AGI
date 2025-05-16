from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(grid[i][j]==grid[i][0] for j in range(w))]
    sep_cols = [j for j in range(w) if all(grid[i][j]==grid[0][j] for i in range(h))]
    br = sep_rows[1]-sep_rows[0]-1
    bc = sep_cols[1]-sep_cols[0]-1
    row_starts = [sep_rows[i]+1 for i in range(len(sep_rows)-1)]
    col_starts = [sep_cols[j]+1 for j in range(len(sep_cols)-1)]
    default = tuple(tuple(grid[row_starts[0]+i][col_starts[0]+j] for j in range(bc)) for i in range(br))
    R = C = None
    patterns = {}
    for i, rs in enumerate(row_starts):
        for j, cs in enumerate(col_starts):
            b = tuple(tuple(grid[rs+i2][cs+j2] for j2 in range(bc)) for i2 in range(br))
            if b!=default:
                patterns[i,j] = b
    # pick the first special
    (R,C), b = next(iter(patterns.items()))
    out = [row[:] for row in grid]
    for i in range(1, R+1):
        rs = row_starts[i]
        cs = col_starts[C]
        for di in range(br):
            for dj in range(bc):
                out[rs+di][cs+dj] = b[di][dj]
    return out