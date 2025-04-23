def solve(grid):
    H, W = len(grid), len(grid[0])
    rows = [i for i in range(H) if all(grid[i][j] == 0 for j in range(W))]
    cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    block_rows = [(rows[i] + 1, rows[i+1]) for i in range(len(rows) - 1)]
    block_cols = [(cols[j] + 1, cols[j+1]) for j in range(len(cols) - 1)]
    nb_r, nb_c = len(block_rows), len(block_cols)
    br_dest, br_src = block_rows[nb_r-1], block_rows[nb_r-2]
    bc_dest, bc_src = block_cols[0], block_cols[nb_c-1]
    bh = br_dest[1] - br_dest[0]
    bw = bc_dest[1] - bc_dest[0]
    color_dest = grid[br_dest[0]][bc_dest[0]]
    mask = [[grid[br_src[0]+i][bc_src[0]+j] != 0 for j in range(1, bw-1)] for i in range(1, bh-1)]
    out = [row[:] for row in grid]
    for i in range(1, bh-1):
        for j in range(1, bw-1):
            if mask[i-1][j-1]:
                out[br_dest[0]+i][bc_dest[0]+j] = color_dest
    return out