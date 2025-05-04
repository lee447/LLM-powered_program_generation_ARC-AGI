def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    pf = []
    for c in range(w):
        if grid[0][c] != 0:
            pf.append(grid[0][c])
        else:
            break
    prefix_len = len(pf)
    dot_c = None
    dot_color = None
    for c in range(prefix_len, w):
        if grid[0][c] != 0:
            dot_c = c
            dot_color = grid[0][c]
            break
    rh = None
    for r in range(h):
        if all(grid[r][c] == grid[r][0] != 0 for c in range(w)):
            rh = r
            stripe_color = grid[r][0]
            break
    ar = ac = acol = None
    for r in range(rh + 1, h):
        for c in range(w):
            if grid[r][c] != 0:
                ar, ac, acol = r, c, grid[r][c]
                break
        if ar is not None:
            break
    rev_pf = pf[::-1]
    if dot_c is not None:
        frames = [dot_color] + rev_pf[:prefix_len - 1]
    else:
        frames = rev_pf[:prefix_len - 1]
    k = len(frames)
    z = (dot_c - prefix_len) if dot_c is not None else 0
    top = ar - k
    left = ac - k
    bottom = ar + k
    right = ac + k
    if dot_c is not None:
        top -= z
        left -= z
        right += z
    for i, color in enumerate(frames):
        if dot_c is not None and i > 0:
            r1 = top + i + z
            c1 = left + i + z
            c2 = right - i - z
        else:
            r1 = top + i
            c1 = left + i
            c2 = right - i
        r2 = bottom - i
        for c in range(c1, c2 + 1):
            out[r1][c] = color
            out[r2][c] = color
        for r in range(r1, r2 + 1):
            out[r][c1] = color
            out[r][c2] = color
    out[ar][ac] = acol
    if dot_c is not None:
        out[0][dot_c] = stripe_color
    return out