def solve(grid):
    h, w = len(grid), len(grid[0])
    left_w = 6
    anchor = grid[0][0]
    stripe_rows = [r for r in range(h) if all(grid[r][c] == anchor for c in range(left_w))]
    bands = []
    for i in range(len(stripe_rows)-1):
        r0, r1 = stripe_rows[i], stripe_rows[i+1]
        rows = list(range(r0+1, r1))
        vals = set()
        counts = []
        for r in rows:
            cnt = 0
            for c in range(left_w, w):
                v = grid[r][c]
                if v != anchor and v != 0:
                    vals.add(v)
                    cnt += 1
            counts.append(cnt)
        color = vals.pop() if vals else anchor
        bands.append((rows, color, counts))
    n = len(bands)
    shifted = [bands[(i+1)%n] for i in range(n)]
    out = [[anchor]*left_w for _ in range(h)]
    for r in stripe_rows:
        out[r] = [anchor]*left_w
    for i, (rows, _, _) in enumerate(bands):
        rows_s, col_s, cnts = shifted[i]
        for j, r in enumerate(rows):
            cr = cnts[j]
            off = (4-cr)//2
            for k in range(cr):
                out[r][1+off+k] = col_s
    return out