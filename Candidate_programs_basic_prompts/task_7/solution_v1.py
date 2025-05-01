from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max(set(sum(grid, [])), key=lambda x: sum(1 for row in grid for v in row if v == x))
    sep_rows = [r for r in range(h) if all(grid[r][c] == bg for c in range(w))]
    sep_cols = [c for c in range(w) if all(grid[r][c] == bg for r in range(h))]
    row_bounds = []
    prev = -1
    for r in sep_rows + [h]:
        if r - prev - 1 > 0:
            row_bounds.append((prev + 1, r))
        prev = r
    col_bounds = []
    prev = -1
    for c in sep_cols + [w]:
        if c - prev - 1 > 0:
            col_bounds.append((prev + 1, c))
        prev = c

    blocks = []
    for br, er in row_bounds:
        for bc, ec in col_bounds:
            pts = [(r - br, c - bc)
                   for r in range(br, er)
                   for c in range(bc, ec)
                   if grid[r][c] != 0 and grid[r][c] != bg]
            if pts:
                color = grid[br + pts[0][0]][bc + pts[0][1]]
                blocks.append(((br, er, bc, ec), tuple(sorted(pts)), color))

    by_shape = {}
    for blk in blocks:
        key = blk[1]
        by_shape.setdefault(key, []).append(blk)

    out = [row[:] for row in grid]
    for shape, blks in by_shape.items():
        cols = set(b[2] for b in blks)
        others = [c for c in cols if c != 1]
        if others and any(b[2] == 1 for b in blks):
            target = others[0]
            for br, er, bc, ec in [(b[0][0], b[0][1], b[0][2], b[0][3]) for b in blks if b[2] == 1]:
                for dr, dc in shape:
                    out[br + dr][bc + dc] = target
    return out