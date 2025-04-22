from typing import List
import collections
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    cnt = collections.Counter()
    for row in grid:
        cnt.update(row)
    items = cnt.most_common()
    bg = items[0][0]
    block = items[1][0]
    row_spans = []
    start = None
    for r in range(n):
        has = any(grid[r][c] == block for c in range(m))
        if has and start is None:
            start = r
        if not has and start is not None:
            row_spans.append((start, r - 1))
            start = None
    if start is not None:
        row_spans.append((start, n - 1))
    col_spans = []
    start = None
    for c in range(m):
        has = any(grid[r][c] == block for r in range(n))
        if has and start is None:
            start = c
        if not has and start is not None:
            col_spans.append((start, c - 1))
            start = None
    if start is not None:
        col_spans.append((start, m - 1))
    sep_rows = set()
    for i in range(len(row_spans) - 1):
        for r in range(row_spans[i][1] + 1, row_spans[i+1][0]):
            sep_rows.add(r)
    sep_cols = set()
    for i in range(len(col_spans) - 1):
        for c in range(col_spans[i][1] + 1, col_spans[i+1][0]):
            sep_cols.add(c)
    row_set = set(r for a,b in row_spans for r in range(a, b+1))
    col_set = set(c for a,b in col_spans for c in range(a, b+1))
    out = [list(row) for row in grid]
    for r in range(n):
        for c in range(m):
            if r in sep_rows or c in sep_cols:
                if r in sep_rows and c in sep_cols:
                    out[r][c] = 2
                elif r in sep_rows:
                    out[r][c] = 2 if c in col_set else 1
                else:
                    out[r][c] = 2 if r in row_set else 1
    return out