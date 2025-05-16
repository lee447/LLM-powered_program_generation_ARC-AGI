def solve(grid):
    h, w = len(grid), len(grid[0])
    # find components of 1's
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and not seen[rr][cc] and grid[rr][cc]==1:
                            seen[rr][cc] = True
                            stack.append((rr,cc))
                comps.append(comp)
    # identify cluster1 (adjacent to 2 or 3) and cluster2
    comp1 = comp2 = None
    for comp in comps:
        found = False
        for r,c in comp:
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                rr,cc = r+dr, c+dc
                if 0<=rr<h and 0<=cc<w and grid[rr][cc] in (2,3):
                    comp1 = comp
                    found = True
                    break
            if found: break
        if found: break
    for comp in comps:
        if comp is not comp1:
            comp2 = comp
    # find stripe1 region
    from collections import deque
    q = deque()
    vis = [[False]*w for _ in range(h)]
    root = None
    for r,c in comp1:
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr,cc = r+dr, c+dc
            if 0<=rr<h and 0<=cc<w and grid[rr][cc] in (2,3):
                root = (rr,cc)
                break
        if root: break
    q.append(root)
    vis[root[0]][root[1]] = True
    stripe = []
    while q:
        r,c = q.popleft()
        stripe.append((r,c))
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr,cc = r+dr, c+dc
            if 0<=rr<h and 0<=cc<w and not vis[rr][cc] and grid[rr][cc] in (2,3):
                vis[rr][cc] = True
                q.append((rr,cc))
    rows = sorted({r for r,c in stripe})
    cols = sorted({c for r,c in stripe})
    height, width = len(rows), len(cols)
    # extract blocks
    blocks = []
    if height > width:
        for r in rows:
            blocks.append([grid[r][c] for c in cols])
    else:
        for c in cols:
            blocks.append([grid[r][c] for r in rows])
    # map values
    mblocks = [[(x if x==2 else 4) for x in blk] for blk in blocks]
    # find cluster2 top row and columns
    top = min(r for r,c in comp2)
    top_cols = sorted(c for r,c in comp2 if r==top)
    L = len(mblocks)
    # draw stripe2 upward from just above top
    for k in range(top):
        r_dest = top-1-k
        blk = mblocks[k % L][:]
        blk_rev = blk[::-1]
        for idx,c in enumerate(top_cols):
            grid[r_dest][c] = blk_rev[idx]
    return grid