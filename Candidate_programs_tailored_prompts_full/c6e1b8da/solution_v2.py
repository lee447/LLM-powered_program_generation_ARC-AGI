def solve(grid):
    h, w = len(grid), len(grid[0])
    bboxes = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                if v not in bboxes:
                    bboxes[v] = [r, c, r, c]
                else:
                    b = bboxes[v]
                    b[0], b[1], b[2], b[3] = min(b[0], r), min(b[1], c), max(b[2], r), max(b[3], c)
    blocks = sorted(
        [(r0, c0, r1, c1, v) for v, (r0, c0, r1, c1) in bboxes.items()],
        key=lambda x: (x[0], x[1])
    )
    out = [[0]*w for _ in range(h)]
    prev_r1 = prev_c1 = None
    for i, (r0, c0, r1, c1, v) in enumerate(blocks):
        bh, bw = r1-r0+1, c1-c0+1
        if i == 0:
            nr0, nc0 = r0, c0
        else:
            nr0, nc0 = prev_r1+1, prev_c1+1
        for dr in range(bh):
            for dc in range(bw):
                out[nr0+dr][nc0+dc] = v
        prev_r1, prev_c1 = nr0+bh-1, nc0+bw-1
    return out