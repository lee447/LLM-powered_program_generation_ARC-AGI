def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    row0 = grid[0]
    # find M0 = length of initial non-zero prefix
    M0 = 0
    while M0 < w and row0[M0] != 0:
        M0 += 1
    # find palette_stop = first index i where row0[i]==0 and row0[i+1]==0
    palette_stop = w
    for i in range(w-1):
        if row0[i] == 0 and row0[i+1] == 0:
            palette_stop = i
            break
    palette = row0[:palette_stop]
    # find marker pixel at r>=2
    rc = cc = None
    for r in range(2, h):
        for c in range(w):
            if grid[r][c] != 0:
                rc, cc = r, c
                break
        if rc is not None:
            break
    # extraneous fix on top row
    for c in range(M0, w):
        if grid[0][c] != 0:
            out[0][c] = grid[1][c]
    # draw rings
    L = len(palette)
    for r in range(h):
        for c in range(w):
            d = abs(r - rc)
            e = abs(c - cc)
            m = d if d >= e else e
            if m < L:
                out[r][c] = palette[m]
    return out