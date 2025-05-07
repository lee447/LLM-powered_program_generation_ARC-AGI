from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = [i for i in range(H) if all(cell == 0 for cell in grid[i])]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    row_blocks = [(zero_rows[k] + 1, zero_rows[k + 1]) for k in range(len(zero_rows) - 1) if zero_rows[k] + 1 < zero_rows[k + 1]]
    col_blocks = [(zero_cols[k] + 1, zero_cols[k + 1]) for k in range(len(zero_cols) - 1) if zero_cols[k] + 1 < zero_cols[k + 1]]
    blocks = []
    for bi, (rs, re) in enumerate(row_blocks):
        for bj, (cs, ce) in enumerate(col_blocks):
            cnt = sum(grid[r][c] == 2 for r in range(rs, re) for c in range(cs, ce))
            blocks.append({'bi': bi, 'bj': bj, 'rs': rs, 're': re, 'cs': cs, 'ce': ce, 'cnt': cnt})
    out = [row[:] for row in grid]
    max_cnt = max(b['cnt'] for b in blocks)
    blocks_max = [b for b in blocks if b['cnt'] == max_cnt]
    n_rb = len(row_blocks)
    if len(blocks_max) > 1:
        pals = [b for b in blocks_max if (b['bi'] + b['bj']) % 2 == 1]
        pals.sort(key=lambda b: (b['bi'], b['bj']))
        for i, b in enumerate(pals):
            if i < 2:
                color = 8
            elif i == 2:
                color = 3
            else:
                break
            for r in range(b['rs'], b['re']):
                for c in range(b['cs'], b['ce']):
                    if out[r][c] == 2:
                        out[r][c] = color
    else:
        b0 = blocks_max[0]
        for r in range(b0['rs'], b0['re']):
            for c in range(b0['cs'], b0['ce']):
                if out[r][c] == 2:
                    out[r][c] = 3
        need = 2
        counts = sorted({b['cnt'] for b in blocks}, reverse=True)
        if len(counts) > 1:
            sc = counts[1]
            sec = [b for b in blocks if b['cnt'] == sc and b['bi'] < n_rb - 1]
            sec.sort(key=lambda b: (b['bj'], b['bi']))
            for b in sec[:need]:
                for r in range(b['rs'], b['re']):
                    for c in range(b['cs'], b['ce']):
                        if out[r][c] == 2:
                            out[r][c] = 8
    return out