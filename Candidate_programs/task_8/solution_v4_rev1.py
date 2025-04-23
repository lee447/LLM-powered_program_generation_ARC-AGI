from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    row_nonzero = [any(grid[r][c] != 0 for c in range(m)) for r in range(n)]
    col_nonzero = [any(grid[r][c] != 0 for r in range(n)) for c in range(m)]
    row_ranges, col_ranges = [], []
    r = 0
    while r < n:
        if row_nonzero[r]:
            start = r
            while r < n and row_nonzero[r]:
                r += 1
            row_ranges.append((start, r - 1))
        else:
            r += 1
    c = 0
    while c < m:
        if col_nonzero[c]:
            start = c
            while c < m and col_nonzero[c]:
                c += 1
            col_ranges.append((start, c - 1))
        else:
            c += 1
    blocks = []
    for bi, (rs, re) in enumerate(row_ranges):
        for bj, (cs, ce) in enumerate(col_ranges):
            block = [grid[i][cs:ce+1] for i in range(rs, re+1)]
            blocks.append((bi, bj, block))
    def classify(block):
        vals = {}
        for row in block:
            for v in row:
                if v != 0:
                    vals[v] = vals.get(v, 0) + 1
        if not vals:
            return None
        shape_color = min(vals, key=lambda k: vals[k])
        h, w = len(block), len(block[0])
        fc = [
            block[0][0] == shape_color,
            block[0][w-1] == shape_color,
            block[h-1][0] == shape_color,
            block[h-1][w-1] == shape_color
        ]
        cnt = sum(fc)
        if cnt == 4:
            return 'full'
        if cnt == 2:
            if fc[0] and fc[1]:
                return 'half_top'
            if fc[2] and fc[3]:
                return 'half_bottom'
            if fc[0] and fc[2]:
                return 'half_left'
            if fc[1] and fc[3]:
                return 'half_right'
        if cnt == 1:
            if fc[0]:
                return 'quarter_tl'
            if fc[1]:
                return 'quarter_tr'
            if fc[2]:
                return 'quarter_bl'
            if fc[3]:
                return 'quarter_br'
        return None
    orient_map = {
        'quarter_tl': (0, 0),
        'quarter_tr': (0, 2),
        'quarter_bl': (2, 0),
        'quarter_br': (2, 2),
        'half_top': (0, 1),
        'half_bottom': (2, 1),
        'half_left': (1, 0),
        'half_right': (1, 2),
        'full': (1, 1)
    }
    result = [[0]*m for _ in range(n)]
    for _, _, block in blocks:
        shape = classify(block)
        ti, tj = orient_map[shape]
        rs, re = row_ranges[ti]
        cs, ce = col_ranges[tj]
        for i in range(re-rs+1):
            for j in range(ce-cs+1):
                result[rs+i][cs+j] = block[i][j]
    return result