from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    row_counts = [sum(1 for v in row if v != 0) for row in grid]
    col_counts = [sum(1 for i in range(h) if grid[i][j] != 0) for j in range(w)]
    stripe_cols = [j for j in range(w) if col_counts[j] > h/2]
    block_rows = [i for i in range(h) if row_counts[i] > w/2]
    stripe_cols.sort()
    block_rows.sort()
    stripe_colors = [next(grid[i][c] for i in range(h) if grid[i][c] != 0) for c in stripe_cols]
    block_colors = [next(grid[r][j] for j in range(w) if grid[r][j] != 0) for r in block_rows]
    hstripe_idx = -1
    for idx, r in enumerate(block_rows):
        if all(grid[r][j] != 0 for j in range(w)) and len(set(grid[r])) == 1:
            hstripe_idx = idx
            break
    R = len(block_rows) * 2 + 1
    C = len(stripe_cols) * 2 + 1
    out = [[0]*C for _ in range(R)]
    for ri in range(R):
        if ri % 2 == 0:
            for ci in range(C):
                if ci % 2 == 1:
                    out[ri][ci] = stripe_colors[ci//2]
        else:
            bi = ri // 2
            if bi == hstripe_idx:
                for ci in range(C):
                    out[ri][ci] = block_colors[bi]
            else:
                for ci in range(C):
                    if ci % 2 == 1:
                        sci = ci // 2
                        r0 = block_rows[bi]
                        c0 = stripe_cols[sci]
                        if grid[r0][c0] == stripe_colors[sci]:
                            out[ri][ci] = stripe_colors[sci]
                        else:
                            out[ri][ci] = block_colors[bi]
                    else:
                        out[ri][ci] = block_colors[bi]
    return out