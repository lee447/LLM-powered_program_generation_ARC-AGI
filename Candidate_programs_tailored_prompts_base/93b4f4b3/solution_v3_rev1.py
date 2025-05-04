def solve(grid):
    H = len(grid)
    W = len(grid[0])
    count = [0] * H
    for i in range(H):
        c = 0
        while c < W and grid[i][c] != 0:
            c += 1
        count[i] = c
    stripe_w = max(count)
    br = sorted([i for i, c in enumerate(count) if c == stripe_w])
    fc = grid[br[0]][0]
    seen = [[False] * W for _ in range(H)]
    clusters = []
    for y in range(H):
        for x in range(stripe_w, W):
            if grid[y][x] != 0 and grid[y][x] != fc and not seen[y][x]:
                col = grid[y][x]
                stack = [(y, x)]
                seen[y][x] = True
                pts = []
                mi = ma = y
                mj = mb = x
                while stack:
                    yy, xx = stack.pop()
                    pts.append((yy, xx))
                    if yy < mi: mi = yy
                    if yy > ma: ma = yy
                    if xx < mj: mj = xx
                    if xx > mb: mb = xx
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = yy + dy, xx + dx
                        if 0 <= ny < H and 0 <= nx < W and not seen[ny][nx] and grid[ny][nx] == col:
                            seen[ny][nx] = True
                            stack.append((ny, nx))
                mask = [(yy - mi, xx - mj) for yy, xx in pts]
                clusters.append((mi, mj, ma, mb, col, mask))
    bands = len(br) - 1
    old = [None] * bands
    for mi, mj, ma, mb, col, mask in clusters:
        cy = (mi + ma) / 2
        for k in range(bands):
            if br[k] < cy < br[k+1]:
                old[k] = (mi, mj, ma, mb, col, mask)
                break
    colors = [old[k][4] for k in range(bands)]
    med = sorted(colors)[bands // 2]
    if bands == 3:
        perm = [1, 2, 0] if fc < med else [2, 1, 0]
    else:
        perm = list(range(bands))
    out = [[fc] * stripe_w for _ in range(H)]
    for i in range(bands):
        mi, mj, ma, mb, col, mask = old[perm[i]]
        shift_y = br[i] + 1
        cw = mb - mj + 1
        shift_x = (stripe_w - cw + 1) // 2
        for dy, dx in mask:
            out[shift_y + dy][shift_x + dx] = col
    return out