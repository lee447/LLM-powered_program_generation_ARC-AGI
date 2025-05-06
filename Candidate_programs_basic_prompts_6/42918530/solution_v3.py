from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    blank_rows = {i for i in range(h) if all(grid[i][j] == 0 for j in range(w))}
    blank_cols = {j for j in range(w) if all(grid[i][j] == 0 for i in range(h))}
    row_segs = []
    i = 0
    while i < h:
        if i not in blank_rows:
            r0 = i
            while i < h and i not in blank_rows:
                i += 1
            row_segs.append((r0, i - 1))
        else:
            i += 1
    col_segs = []
    j = 0
    while j < w:
        if j not in blank_cols:
            c0 = j
            while j < w and j not in blank_cols:
                j += 1
            col_segs.append((c0, j - 1))
        else:
            j += 1
    out = [row[:] for row in grid]
    blocks_by_color = {}
    for r0, r1 in row_segs:
        for c0, c1 in col_segs:
            c = grid[r0][c0]
            if c == 0:
                c = next((grid[r0][j] for j in range(c0, c1+1) if grid[r0][j] != 0), 0)
            if c == 0:
                continue
            interior = [out[i][c0+1:c1] for i in range(r0+1, r1)]
            cnt = sum(1 for row in interior for x in row if x == c)
            blocks_by_color.setdefault(c, []).append({
                'r0': r0, 'r1': r1, 'c0': c0, 'c1': c1,
                'interior': interior, 'count': cnt
            })
    for c, blks in blocks_by_color.items():
        if len(blks) < 2:
            continue
        tpl = max(blks, key=lambda b: b['count'])
        if tpl['count'] == 0:
            continue
        tr0, tc0 = tpl['r0']+1, tpl['c0']+1
        pat = tpl['interior']
        for b in blks:
            if b is tpl:
                continue
            for dx in range(len(pat)):
                for dy in range(len(pat[0])):
                    if pat[dx][dy] == c:
                        out[b['r0']+1+dx][b['c0']+1+dy] = c
    return out