from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else (0, 0)
    row_spans, col_spans = {}, {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                if v == 2:
                    row_spans.setdefault(r, []).append((c, c))
                    col_spans.setdefault(c, []).append((r, r))
                if c + 2 < w and grid[r][c] == grid[r][c+1] == grid[r][c+2] != 0 and (c == 0 or grid[r][c-1] != grid[r][c]):
                    row_spans.setdefault(r, []).append((c, c+2))
                    for cc in (c, c+1, c+2):
                        col_spans.setdefault(cc, []).append((r, r))
                if r + 2 < h and grid[r][c] == grid[r+1][c] == grid[r+2][c] != 0 and (r == 0 or grid[r-1][c] != grid[r][c]):
                    col_spans.setdefault(c, []).append((r, r+2))
                    for rr in (r, r+1, r+2):
                        row_spans.setdefault(rr, []).append((c, c))
    out = [row[:] for row in grid]
    for r, spans in row_spans.items():
        if len(spans) < 2: continue
        spans.sort(key=lambda x: x[0])
        for i in range(len(spans) - 1):
            e = spans[i][1]
            s = spans[i+1][0]
            for cc in range(e+1, s):
                if out[r][cc] == 0:
                    out[r][cc] = 2
    for c, spans in col_spans.items():
        if len(spans) < 2: continue
        spans.sort(key=lambda x: x[0])
        for i in range(len(spans) - 1):
            e = spans[i][1]
            s = spans[i+1][0]
            for rr in range(e+1, s):
                if out[rr][c] == 0:
                    out[rr][c] = 2
    return out