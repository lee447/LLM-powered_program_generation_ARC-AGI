def solve(grid):
    from collections import deque, defaultdict
    h, w = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    def inb(r,c):
        return 0<=r<h and 0<=c<w
    # find all 1‐components
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j]=True
                cells = []
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    for dr,dc in dirs:
                        rr,cc = r+dr, c+dc
                        if inb(rr,cc) and not vis[rr][cc] and grid[rr][cc]==1:
                            vis[rr][cc]=True
                            q.append((rr,cc))
                # bounding box
                rs = [r for r,c in cells]; cs = [c for r,c in cells]
                r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
                comps.append((cells, r0,r1,c0,c1))
    # for each comp, look for a seed >1 adjacent to it
    seed_for = {}
    for idx,(_,r0,r1,c0,c1) in enumerate(comps):
        color = None
        for r in range(r0-1, r1+2):
            for c in range(c0-1, c1+2):
                if inb(r,c) and grid[r][c]>1:
                    color = grid[r][c]
        if color is not None:
            seed_for[idx] = color
    # group comps by shape mask
    shape_map = defaultdict(list)
    for idx,(cells,r0,r1,c0,c1) in enumerate(comps):
        h0,h1,cw = r1-r0+1, c1-c0+1, c1-c0+1
        mask = ['']*h0
        s = [['0']*cw for _ in range(h0)]
        for r,c in cells:
            s[r-r0][c-c0] = '1'
        for ii in range(h0): mask[ii] = ''.join(s[ii])
        key = (h0,cw,tuple(mask))
        shape_map[key].append(idx)
    # output copy
    out = [row[:] for row in grid]
    # for each shape group with a seed comp, propagate color
    for key, idxs in shape_map.items():
        # find any idx in this group that has a seed
        seed = None
        for idx in idxs:
            if idx in seed_for:
                seed = seed_for[idx]
                break
        if seed is None: continue
        # color all comps in this group
        for idx in idxs:
            cells,_,_,_,_ = comps[idx]
            for r,c in cells:
                out[r][c] = seed
    return out