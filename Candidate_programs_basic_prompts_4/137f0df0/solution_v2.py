from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bg = 0
    has_row = [any(cell != bg for cell in row) for row in grid]
    has_col = [any(grid[i][j] != bg for i in range(H)) for j in range(W)]
    def get_clusters(flag):
        blocks, zeros = [], []
        i = 0
        while i < len(flag):
            if flag[i]:
                s = i
                while i < len(flag) and flag[i]:
                    i += 1
                blocks.append((s, i - 1))
            else:
                s = i
                while i < len(flag) and not flag[i]:
                    i += 1
                zeros.append((s, i - 1))
        return blocks, zeros
    row_blocks, row_zeros = get_clusters(has_row)
    col_blocks, col_zeros = get_clusters(has_col)
    interior_sep_rows = set()
    boundary_sep_rows = set()
    for zs, ze in row_zeros:
        before = any(be < zs for bs, be in row_blocks)
        after = any(bs > ze for bs, be in row_blocks)
        if before and after:
            for i in range(zs, ze + 1):
                interior_sep_rows.add(i)
        else:
            for i in range(zs, ze + 1):
                boundary_sep_rows.add(i)
    interior_sep_cols = set()
    boundary_sep_cols = set()
    for zs, ze in col_zeros:
        before = any(be < zs for bs, be in col_blocks)
        after = any(bs > ze for bs, be in col_blocks)
        if before and after:
            for j in range(zs, ze + 1):
                interior_sep_cols.add(j)
        else:
            for j in range(zs, ze + 1):
                boundary_sep_cols.add(j)
    block_cols = [j for j, b in enumerate(has_col) if b]
    first_block_col, last_block_col = min(block_cols), max(block_cols)
    out = [row[:] for row in grid]
    for i in interior_sep_rows:
        for j in range(W):
            out[i][j] = 2 if first_block_col <= j <= last_block_col else 1
    for j in interior_sep_cols:
        for i in range(H):
            if has_row[i] or i in interior_sep_rows:
                out[i][j] = 2
            elif i in boundary_sep_rows:
                out[i][j] = 1
    return out