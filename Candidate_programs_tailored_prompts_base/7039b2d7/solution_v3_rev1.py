from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    from collections import Counter
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = Counter(flat).most_common(1)[0][0]
    # find stripe color
    rows_u = [i for i in range(h) if len(set(grid[i])) == 1]
    stripe_color = None
    for i in rows_u:
        c = grid[i][0]
        if c != bg:
            stripe_color = c
            break
    if stripe_color is None:
        cols_u = [j for j in range(w) if len({grid[i][j] for i in range(h)}) == 1]
        for j in cols_u:
            c = grid[0][j]
            if c != bg:
                stripe_color = c
                break
    if stripe_color is None:
        stripe_color = bg
    stripe_rows = [i for i in rows_u if grid[i][0] == stripe_color]
    cols_u = [j for j in range(w) if len({grid[i][j] for i in range(h)}) == 1]
    stripe_cols = [j for j in cols_u if grid[0][j] == stripe_color]
    stripe_rows.sort()
    stripe_cols.sort()
    # select the two stripes that bound the "second" cell if many, else the two we have
    if len(stripe_rows) >= 3:
        r0, r1 = stripe_rows[1], stripe_rows[2]
        hr = r1 - r0 - 1
    elif len(stripe_rows) == 2:
        r0, r1 = stripe_rows[0], stripe_rows[1]
        hr = r1 - r0
    else:
        return []
    if len(stripe_cols) >= 3:
        c0, c1 = stripe_cols[1], stripe_cols[2]
        wc = c1 - c0 - 1
    elif len(stripe_cols) == 2:
        c0, c1 = stripe_cols[0], stripe_cols[1]
        wc = c1 - c0 - 1
    else:
        return []
    return [[bg]*wc for _ in range(hr)]