def solve(grid):
    n, m = len(grid), len(grid[0])
    stripe_col = next(c for c in range(m) if len({grid[r][c] for r in range(n)}) == 1)
    stripe_color = grid[0][stripe_col]
    stripe_row = next(r for r in range(n) if sum(1 for c in range(m) if c != stripe_col and grid[r][c] == stripe_color) > 1)
    def region(r0, r1, c0, c1):
        return [row[c0:c1+1] for row in grid[r0:r1+1]]
    def bg(col):
        f = {}
        for x in col:
            f[x] = f.get(x,0)+1
        return max(f, key=f.get)
    def anchors(reg):
        h, w = len(reg), len(reg[0])
        b = bg(x for row in reg for x in row)
        a = []
        for i in range(min(h, w)):
            if reg[i][i] != b:
                a.append(reg[i][i])
            else:
                break
        return a
    r1, r2 = 0, stripe_row-1
    r3, r4 = stripe_row+1, n-1
    c1, c2 = 0, stripe_col-1
    c3, c4 = stripe_col+1, m-1
    R1 = region(r1, r2, c1, c2)
    R2 = region(r1, r2, c3, c4)
    R3 = region(r3, r4, c1, c2)
    R4 = region(r3, r4, c3, c4)
    A1 = anchors(R1)
    A2 = anchors(R2)
    A4 = anchors(R4)
    A3 = A1 if not anchors(R3) else anchors(R3)
    def fill(reg_len, reg_wid, A, i, j):
        layer = min(i, j, reg_len-1-i, reg_wid-1-j)
        return A[layer % len(A)]
    out = [[0]*m for _ in range(n)]
    for r in range(n):
        out[r][stripe_col] = stripe_color
    for c in range(m):
        out[stripe_row][c] = stripe_color
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            out[r][c] = fill(r2-r1+1, c2-c1+1, A1, r-r1, c-c1)
    for r in range(r1, r2+1):
        for c in range(c3, c4+1):
            out[r][c] = fill(r2-r1+1, c4-c3+1, A2, r-r1, c-c3)
    for r in range(r3, r4+1):
        for c in range(c1, c2+1):
            out[r][c] = fill(r4-r3+1, c2-c1+1, A3, r-r3, c-c1)
    for r in range(r3, r4+1):
        for c in range(c3, c4+1):
            out[r][c] = fill(r4-r3+1, c4-c3+1, A4, r-r3, c-c3)
    return out