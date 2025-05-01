def solve(grid):
    H, W = len(grid), len(grid[0])
    # find marker color: the one forming a perfect filled rectangle
    from collections import defaultdict
    regs = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v == 0: continue
            regs.setdefault(v, [r,r,c,c,0])
            regs[v][0] = min(regs[v][0], r)
            regs[v][1] = max(regs[v][1], r)
            regs[v][2] = min(regs[v][2], c)
            regs[v][3] = max(regs[v][3], c)
            regs[v][4] += 1
    marker = None
    for v,(r0,r1,c0,c1,cnt) in regs.items():
        if (r1-r0+1)*(c1-c0+1) == cnt and r1-r0>0 and c1-c0>0:
            marker = (v, r0, r1, c0, c1)
            break
    _, r0, r1, c0, c1 = marker
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    # extract the block immediately above the marker and to its left
    out = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(grid[r0-1-i][c0-1-j])
        out.append(row[::-1])
    return out