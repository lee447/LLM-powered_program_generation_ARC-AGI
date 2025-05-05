def solve(grid):
    h, w = len(grid), len(grid[0])
    row_counts = [sum(1 for v in row if v != 0) for row in grid]
    col_counts = [sum(1 for i in range(h) if grid[i][j] != 0) for j in range(w)]
    stripe_cols = [j for j in range(w) if col_counts[j] > h/2]
    block_rows = [i for i in range(h) if row_counts[i] > w/2]
    stripe_cols.sort()
    block_rows.sort()
    stripe_colors = []
    for c in stripe_cols:
        for i in range(h):
            if grid[i][c] != 0:
                stripe_colors.append(grid[i][c])
                break
    block_colors = []
    for r in block_rows:
        for j in range(w):
            if grid[r][j] != 0:
                block_colors.append(grid[r][j])
                break
    hstripe_idx = None
    for idx, r in enumerate(block_rows):
        if all(grid[r][j] != 0 for j in range(w)) and len(set(grid[r])) == 1:
            hstripe_idx = idx
            break
    R = len(block_rows)*2 + 1
    C = len(stripe_cols)*2 + 1
    out = [[0]*C for _ in range(R)]
    for ri in range(R):
        for ci in range(C):
            if ri%2==1 and ci%2==1 and hstripe_idx is not None and ri//2 == hstripe_idx:
                out[ri][ci] = block_colors[ri//2]
            elif ci%2==1:
                idx = ci//2
                out[ri][ci] = stripe_colors[idx]
            elif ri%2==1:
                idx = ri//2
                out[ri][ci] = block_colors[idx]
    return out