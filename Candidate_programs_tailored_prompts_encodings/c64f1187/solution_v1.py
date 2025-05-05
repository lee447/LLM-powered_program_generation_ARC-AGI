from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    starts = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5:
                starts.append(r)
                break
    stripes = sorted(set(starts))
    blocks = []
    all_colors = []
    for r in stripes:
        cols = [c for c in range(w-1) if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5]
        cols.sort()
        blocks.append(cols)
        row_colors = []
        for c in cols:
            colv = None
            for dr in (0,1):
                for dc in (0,1):
                    v = grid[r+dr][c+dc]
                    if v!=5 and v!=0:
                        colv = v
            row_colors.append(colv)
        all_colors.append(row_colors)
    if not blocks:
        return []
    block_count = len(blocks[0])
    stripe_count = len(stripes)
    H = stripe_count*3 - 1
    W = block_count*3 - 1
    out = [[0]*W for _ in range(H)]
    for i, row_colors in enumerate(all_colors):
        ro = i*3
        for k, c in enumerate(row_colors):
            if c:
                co = k*3
                out[ro][co] = c
                out[ro][co+1] = c
                out[ro+1][co] = c
                out[ro+1][co+1] = c
    return out