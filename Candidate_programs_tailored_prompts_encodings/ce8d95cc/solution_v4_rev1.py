from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    stripes = [j for j in range(w) if all(grid[i][j] != 0 for i in range(h))]
    stripe_colors = {j: next(grid[i][j] for i in range(h) if grid[i][j] != 0) for j in stripes}
    blocks = [i for i in range(h) if all(grid[i][j] != 0 for j in range(w))]
    block_colors = {i: next(grid[i][j] for j in range(w) if j not in stripes and grid[i][j] != 0) for i in blocks}
    comp_cols, prev = [], -1
    for j in sorted(stripes):
        if j - prev > 1: comp_cols.append(('bg', None))
        comp_cols.append(('stripe', j))
        prev = j
    if prev < w - 1: comp_cols.append(('bg', None))
    comp_rows, prev = [], -1
    for i in sorted(blocks):
        if i - prev > 1: comp_rows.append(('bg', None))
        comp_rows.append(('block', i))
        prev = i
    if prev < h - 1: comp_rows.append(('bg', None))
    out = []
    for rtype, ri in comp_rows:
        row = []
        for ctype, cj in comp_cols:
            if rtype == 'block':
                if ctype == 'stripe':
                    sc = stripe_colors[cj]
                    row.append(sc if grid[ri][cj] == sc else block_colors[ri])
                else:
                    row.append(block_colors[ri])
            else:
                row.append(stripe_colors[cj] if ctype == 'stripe' else 0)
        out.append(row)
    return out