from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripe_rows = []
    for r in range(h-1):
        for c in range(w-1):
            cnt = 0
            for dr in (0,1):
                for dc in (0,1):
                    if grid[r+dr][c+dc] == 5:
                        cnt += 1
            if cnt >= 3:
                stripe_rows.append(r)
                break
    stripes = []
    i = 0
    while i < len(stripe_rows):
        r = stripe_rows[i]
        stripes.append(r)
        j = i + 1
        while j < len(stripe_rows) and stripe_rows[j] <= r + 1:
            j += 1
        i = j
    if not stripes:
        return []
    first_r = stripes[0]
    block_cols = []
    for c in range(w-1):
        cnt = 0
        for dr in (0,1):
            for dc in (0,1):
                if grid[first_r+dr][c+dc] == 5:
                    cnt += 1
        if cnt >= 3:
            block_cols.append(c)
    stripe_count = len(stripes)
    block_count = len(block_cols)
    H = stripe_count*3 - 1
    W = block_count*3 - 1
    out = [[0]*W for _ in range(H)]
    for i, r in enumerate(stripes):
        for j, c in enumerate(block_cols):
            colv = None
            for dr in (0,1):
                for dc in (0,1):
                    v = grid[r+dr][c+dc]
                    if v != 5 and v != 0:
                        colv = v
            if colv is not None:
                ro = i*3
                co = j*3
                out[ro][co] = colv
                out[ro][co+1] = colv
                out[ro+1][co] = colv
                out[ro+1][co+1] = colv
    return out