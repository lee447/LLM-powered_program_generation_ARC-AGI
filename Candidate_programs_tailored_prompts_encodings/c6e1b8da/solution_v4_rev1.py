from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    # find the horizontal divider
    div_r = None
    for r in range(1, H-1):
        if all(v==0 for v in grid[r]) and any(grid[r-1][c]!=0 for c in range(W)) and any(grid[r+1][c]!=0 for c in range(W)):
            div_r = r
            break
    if div_r is None:
        div_r = H//2
    # collect regions
    regs = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v==0: continue
            if v not in regs:
                regs[v] = [r, r, c, c]
            else:
                regs[v][0] = min(regs[v][0], r)
                regs[v][1] = max(regs[v][1], r)
                regs[v][2] = min(regs[v][2], c)
                regs[v][3] = max(regs[v][3], c)
    out = [[0]*W for _ in range(H)]
    # process top half and bottom half separately
    for top in (True, False):
        if top:
            block = [(v,b) for v,b in regs.items() if b[1] < div_r]
        else:
            block = [(v,b) for v,b in regs.items() if b[0] > div_r]
        if not block: continue
        # sort by left edge
        block.sort(key=lambda x: x[1][2])
        # place first block at its own place
        v0,(r0_0,r1_0,c0_0,c1_0) = block[0]
        h0 = r1_0 - r0_0 + 1
        # fill bounding rectangle for first block
        for rr in range(r0_0, r1_0+1):
            for cc in range(c0_0, c1_0+1):
                out[rr][cc] = v0
        # if there's a second block, shift it to avoid overlap
        if len(block)>1:
            v1,(r0_1,r1_1,c0_1,c1_1) = block[1]
            # compute overlap rows
            ov0 = max(r0_0, r0_1)
            ov1 = min(r1_0, r1_1)
            shift = 0
            if ov0 <= ov1:
                # in overlapping rows, look at width of first block
                w0 = 0
                for rr in range(ov0, ov1+1):
                    # count how many of v0 on that row in original
                    cnt = sum(1 for cc in range(c0_0, c1_0+1) if grid[rr][cc]==v0)
                    w0 = max(w0, cnt)
                shift = w0
            # place second block shifted
            nc0 = c0_1 + shift
            nc1 = nc0 + (c1_1-c0_1)
            for rr in range(r0_1, r1_1+1):
                for cc in range(nc0, nc1+1):
                    out[rr][cc] = v1
    return out