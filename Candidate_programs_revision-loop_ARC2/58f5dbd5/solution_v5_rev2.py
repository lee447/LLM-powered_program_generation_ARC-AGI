from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r, c = len(grid), len(grid[0])
    b = grid[0][0]
    sep_rows = [i for i in range(r) if all(grid[i][j] == b for j in range(c))]
    sep_cols = [j for j in range(c) if all(grid[i][j] == b for i in range(r))]
    sep_rows.sort()
    sep_cols.sort()
    row_segs = []
    for i in range(len(sep_rows) - 1):
        s, e = sep_rows[i] + 1, sep_rows[i + 1] - 1
        if s <= e:
            row_segs.append((s, e))
    col_segs = []
    for j in range(len(sep_cols) - 1):
        s, e = sep_cols[j] + 1, sep_cols[j + 1] - 1
        if s <= e:
            col_segs.append((s, e))
    if b > 4:
        max_c = max(e - s + 1 for s, e in col_segs)
        sel_c = [seg for seg in col_segs if seg[1] - seg[0] + 1 == max_c][:1]
        keep_cols = set()
        for s, e in sel_c:
            if s - 1 >= 0: keep_cols.add(s - 1)
            for x in range(s, e + 1): keep_cols.add(x)
            if e + 1 < c: keep_cols.add(e + 1)
        keep_cols = sorted(j for j in keep_cols if 0 <= j < c)
        keep_rows = list(range(r))
    elif b > 1:
        max_r = max(e - s + 1 for s, e in row_segs)
        sel_r = [seg for seg in row_segs if seg[1] - seg[0] + 1 == max_r][:1]
        keep_rows = set()
        for s, e in sel_r:
            if s - 1 >= 0: keep_rows.add(s - 1)
            for x in range(s, e + 1): keep_rows.add(x)
            if e + 1 < r: keep_rows.add(e + 1)
        keep_rows = sorted(i for i in keep_rows if 0 <= i < r)
        keep_cols = list(range(c))
    else:
        max_r = max(e - s + 1 for s, e in row_segs)
        sel_r = [seg for seg in row_segs if seg[1] - seg[0] + 1 == max_r]
        keep_rows = set()
        for s, e in sel_r:
            if s - 1 >= 0: keep_rows.add(s - 1)
            for x in range(s, e + 1): keep_rows.add(x)
            if e + 1 < r: keep_rows.add(e + 1)
        keep_rows = sorted(i for i in keep_rows if 0 <= i < r)
        max_c = max(e - s + 1 for s, e in col_segs)
        sel_c = [seg for seg in col_segs if seg[1] - seg[0] + 1 == max_c]
        keep_cols = set()
        for s, e in sel_c:
            if s - 1 >= 0: keep_cols.add(s - 1)
            for x in range(s, e + 1): keep_cols.add(x)
            if e + 1 < c: keep_cols.add(e + 1)
        keep_cols = sorted(j for j in keep_cols if 0 <= j < c)
    return [[grid[i][j] for j in keep_cols] for i in keep_rows]