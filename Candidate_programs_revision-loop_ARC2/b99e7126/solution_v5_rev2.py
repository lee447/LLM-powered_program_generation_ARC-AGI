from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if len(set(grid[i])) == 1]
    sep_cols = [j for j in range(w) if len({grid[i][j] for i in range(h)}) == 1]
    br = sep_rows[1] - sep_rows[0] - 1
    bc = sep_cols[1] - sep_cols[0] - 1
    row_starts = [sep_rows[k] + 1 for k in range(len(sep_rows) - 1)]
    col_starts = [sep_cols[k] + 1 for k in range(len(sep_cols) - 1)]
    default = tuple(tuple(grid[row_starts[0] + i][col_starts[0] + j] for j in range(bc)) for i in range(br))
    variants = {}
    positions = {}
    for i, rs in enumerate(row_starts):
        for j, cs in enumerate(col_starts):
            block = tuple(tuple(grid[rs + di][cs + dj] for dj in range(bc)) for di in range(br))
            if block != default:
                variants[block] = variants.get(block, 0) + 1
                positions.setdefault(block, []).append((i, j))
    b = max(variants.items(), key=lambda x: x[1])[0]
    js = sorted({j for _, j in positions[b]})
    R = positions[b][0][0]
    parity = R % 2
    out = [row[:] for row in grid]
    for i, rs in enumerate(row_starts):
        if i % 2 == parity and i != R:
            for j in js:
                cs = col_starts[j]
                for di in range(br):
                    for dj in range(bc):
                        out[rs + di][cs + dj] = b[di][dj]
    return out