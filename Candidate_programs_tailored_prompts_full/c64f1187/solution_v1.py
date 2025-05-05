from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bands = []
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 5:
                bands.append(i)
                break
    bands = bands[:3]
    block_positions = []
    r0 = bands[0]
    for j in range(w-1):
        if grid[r0][j] == grid[r0][j+1] == grid[r0+1][j] == grid[r0+1][j+1] == 5:
            block_positions.append(j)
    nb = len(block_positions)
    values = []
    for bi in range(3):
        r = bands[bi]
        row_vals = [None] * nb
        for k, j in enumerate(block_positions):
            v = None
            for dr in (0, 1):
                for dc in (0, 1):
                    c = grid[r+dr][j+dc]
                    if c != 5:
                        v = c
            row_vals[k] = v
        values.append(row_vals)
    out_h = 8
    out_w = nb*2 + (nb-1)
    out = [[0]*out_w for _ in range(out_h)]
    for bi in range(3):
        ro = bi*3
        for k in range(nb):
            v = values[bi][k]
            if v is None:
                continue
            co = k*3
            for dr in (0, 1):
                for dc in (0, 1):
                    out[ro+dr][co+dc] = v
    return out