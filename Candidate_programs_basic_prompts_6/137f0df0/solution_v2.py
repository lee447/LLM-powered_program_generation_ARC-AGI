from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=lambda k: freq[k])
    sep_rows = [r for r in range(h) if all(grid[r][c] == bg for c in range(w))]
    sep_cols = [c for c in range(w) if all(grid[r][c] == bg for r in range(h))]
    block_rows = [r for r in range(h) if r not in sep_rows]
    block_cols = [c for c in range(w) if c not in sep_cols]
    first_br, last_br = min(block_rows), max(block_rows)
    first_bc, last_bc = min(block_cols), max(block_cols)
    top_sep_rows = {r for r in sep_rows if r < first_br}
    bottom_sep_rows = {r for r in sep_rows if r > last_br}
    border_sep_rows = top_sep_rows | bottom_sep_rows
    interior_sep_rows = set(sep_rows) - border_sep_rows
    left_sep_cols = {c for c in sep_cols if c < first_bc}
    right_sep_cols = {c for c in sep_cols if c > last_bc}
    border_sep_cols = left_sep_cols | right_sep_cols
    interior_sep_cols = set(sep_cols) - border_sep_cols
    res = [row[:] for row in grid]
    inner, outer = 2, 1
    for r in interior_sep_rows:
        for c in range(w):
            res[r][c] = outer if c in border_sep_cols else inner
    for c in interior_sep_cols:
        for r in range(h):
            res[r][c] = outer if r in border_sep_rows else inner
    return res