def solve(grid):
    h, w = len(grid), len(grid[0])
    boxes = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                if v not in boxes:
                    boxes[v] = [r, c, r, c]
                else:
                    b = boxes[v]
                    b[0] = min(b[0], r)
                    b[1] = min(b[1], c)
                    b[2] = max(b[2], r)
                    b[3] = max(b[3], c)
    blocks = sorted([(b[0], b[1], b[2], b[3], v) for v,b in boxes.items()])
    out = [[0]*w for _ in range(h)]
    prev_br_r, prev_br_c = None, None
    for i, (r0,c0,r1,c1,v) in enumerate(blocks):
        hgt, wid = r1-r0+1, c1-c0+1
        if i==0:
            nr, nc = r0, c0
        else:
            nr = prev_br_r+1
            nc = prev_br_c+1
        for dr in range(hgt):
            for dc in range(wid):
                out[nr+dr][nc+dc] = v
        prev_br_r = nr + hgt - 1
        prev_br_c = nc + wid - 1
    return out