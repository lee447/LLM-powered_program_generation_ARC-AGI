from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    row_sep = [i for i in range(h) if all(x == 0 for x in grid[i])]
    col_sep = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    bh = row_sep[1] - row_sep[0] - 1
    bw = col_sep[1] - col_sep[0] - 1
    r0, c0 = row_sep[0] + 1, col_sep[0] + 1
    bg = grid[r0][c0]
    shape = []
    for dr in range(bh):
        for dc in range(bw):
            v = grid[r0 + dr][c0 + dc]
            if v != bg:
                shape.append((dr, dc, v))
    for bi in range(len(row_sep) - 1):
        for bj in range(len(col_sep) - 1):
            rs = row_sep[bi] + 1
            cs = col_sep[bj] + 1
            marker = None
            for dr, dc, rv in shape:
                v = grid[rs + dr][cs + dc]
                if v != rv and v != bg:
                    marker = (dr, dc)
                    break
            if marker is not None:
                for dr, dc, rv in shape:
                    if (dr, dc) != marker and grid[rs + dr][cs + dc] != rv:
                        grid[rs + dr][cs + dc] = rv
    return grid