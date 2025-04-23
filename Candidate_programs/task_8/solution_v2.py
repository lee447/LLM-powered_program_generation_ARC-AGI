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
    bh = row_ranges[0][1] - row_ranges[0][0] + 1
    bw = col_ranges[0][1] - col_ranges[0][0] + 1
    blocks = []
    for bi, (rs, re) in enumerate(row_ranges):
        for bj, (cs, ce) in enumerate(col_ranges):
            block = [grid[r][cs:ce+1] for r in range(rs, re+1)]
            blocks.append((bi, bj, block))
    def classify(block):
        h, w = len(block), len(block[0])
        mid = h // 2
        inner = block[mid][mid]
        vals = {v for row in block for v in row if v != 0}
        outer = (vals - {inner}).pop()
        f = [
            block[0][0] == outer,
            block[0][w-1] == outer,
            block[h-1][0] == outer,
            block[h-1][w-1] == outer
        ]
        cnt = sum(f)
        if cnt == 4:
            return 'full'
        if cnt == 2:
            if f[0] and f[1]: return 'half_top'
            if f[2] and f[3]: return 'half_bottom'
            if f[0] and f[2]: return 'half_left'
            if f[1] and f[3]: return 'half_right'
        if cnt == 1:
            if f[0]: return 'quarter_tl'
            if f[1]: return 'quarter_tr'
            if f[2]: return 'quarter_bl'
            if f[3]: return 'quarter_br'
        return None
    orient_positions = {
        'full': [(1,1)],
        'half_top': [(0,1)],
        'half_bottom': [(2,1)],
        'half_left': [(1,0)],
        'half_right': [(1,2)],
        'quarter_tl': [(0,0)],
        'quarter_tr': [(0,2)],
        'quarter_bl': [(2,0)],
        'quarter_br': [(2,2)]
    }
    result = [[0]*m for _ in range(n)]
    for bi, bj, block in blocks:
        orient = classify(block)
        ti, tj = orient_positions[orient].pop(0)
        rs, re = row_ranges[ti]
        cs, ce = col_ranges[tj]
        for i in range(re-rs+1):
            for j in range(ce-cs+1):
                result[rs+i][cs+j] = block[i][j]
    return result