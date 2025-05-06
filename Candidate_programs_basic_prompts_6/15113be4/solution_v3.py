def solve(grid):
    h, w = len(grid), len(grid[0])
    sep = 4
    rows = [i for i in range(h) if all(grid[i][j] == sep for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j] == sep for i in range(h))]
    br = [ -1 ] + rows + [h]
    bc = [ -1 ] + cols + [w]
    out = [row[:] for row in grid]
    # find highlight color
    used = set()
    for r in range(h):
        for c in range(w):
            used.add(grid[r][c])
    highlight = next(c for c in range(10) if c not in used)
    for bi in range(len(br)-1):
        for bj in range(len(bc)-1):
            r0, r1 = br[bi]+1, br[bi+1]
            c0, c1 = bc[bj]+1, bc[bj+1]
            if r1 - r0 != 3 or c1 - c0 != 3: continue
            # for each diagonal direction
            for dr, dc in ((1,1),(-1,1)):
                for i in range(3):
                    for j in range(3):
                        r, c = r0+i, c0+j
                        rr, cc = r+dr, c+dc
                        if r0 <= rr < r1 and c0 <= cc < c1:
                            v = grid[r][c]
                            if v != sep and v == grid[rr][cc]:
                                out[r][c] = highlight
                                out[rr][cc] = highlight
    return out