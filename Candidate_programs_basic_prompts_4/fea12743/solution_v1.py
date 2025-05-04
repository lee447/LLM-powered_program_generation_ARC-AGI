def solve(grid):
    H, W = len(grid), len(grid[0])
    sep_rows = [i for i in range(H) if all(grid[i][j] == 0 for j in range(W))]
    sep_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    rseps = [0] + sep_rows + [H]
    cseps = [0] + sep_cols + [W]
    blocks = []
    for bi in range(len(rseps) - 1):
        r0, r1 = rseps[bi], rseps[bi+1]
        if r1 - r0 <= 1: continue
        for bj in range(len(cseps) - 1):
            c0, c1 = cseps[bj], cseps[bj+1]
            if c1 - c0 <= 1: continue
            s = 0
            for i in range(r0+1, r1):
                for j in range(c0+1, c1):
                    if grid[i][j] != 0: s += 1
            blocks.append(((bi, bj), r0+1, r1, c0+1, c1, s))
    if not blocks:
        return grid
    mn = min(blocks, key=lambda x: x[5])[0]
    mx = max(blocks, key=lambda x: x[5])[0]
    R = max(bi for (bi, bj), *_ in blocks) + 1
    C = max(bj for (bi, bj), *_ in blocks) + 1
    from collections import deque
    dq = deque([mn])
    prev = {mn: None}
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while dq:
        u = dq.popleft()
        if u == mx:
            break
        for d in dirs:
            v = (u[0]+d[0], u[1]+d[1])
            if 0 <= v[0] < R and 0 <= v[1] < C and v not in prev:
                prev[v] = u
                dq.append(v)
    path = []
    cur = mx
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    block_map = {pos: (r0, r1, c0, c1) for pos, r0, r1, c0, c1, _ in blocks}
    out = [row[:] for row in grid]
    for idx, pos in enumerate(path):
        color = 3 if idx == len(path) - 1 else 8
        r0, r1, c0, c1 = block_map[pos]
        for i in range(r0, r1):
            for j in range(c0, c1):
                if out[i][j] != 0:
                    out[i][j] = color
    return out