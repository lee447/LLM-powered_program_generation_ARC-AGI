def solve(grid):
    R, C = len(grid), len(grid[0])
    def find_2x2(col):
        res = []
        for r in range(R-1):
            for c in range(C-1):
                if grid[r][c]==col and grid[r][c+1]==col and grid[r+1][c]==col and grid[r+1][c+1]==col:
                    res.append((r,c))
        return res
    # 1) detect grey 2×2 clusters
    grey = 5
    clusters = find_2x2(grey)
    # 2) detect header if no grey cluster
    if not clusters:
        header_rows = 0
        for r in range(R):
            if len(set(grid[r]))>C//2:
                header_rows +=1
            else:
                break
        header_cols = 0
        for c in range(C):
            vals = {grid[r][c] for r in range(header_rows)}
            if len(vals)>1:
                header_cols +=1
            else:
                break
        cluster_top, cluster_left = 0, 0
        cluster_bot, cluster_right = header_rows-1, header_cols-1
    else:
        # pick topmost grey cluster
        r0,c0 = min(clusters)
        cluster_top, cluster_left = r0, c0
        cluster_bot, cluster_right = r0+1, c0+1
    # 3) detect stripe
    # horizontal candidates
    h_runs = []
    for r in range(R):
        cnt = {}
        for v in grid[r]:
            cnt[v] = cnt.get(v,0)+1
        for v,n in cnt.items():
            if n>=C*0.6 and n<C:
                h_runs.append((r,v))
    # vertical candidates
    v_runs = []
    for c in range(C):
        cnt = {}
        for r in range(R):
            v = grid[r][c]
            cnt[v] = cnt.get(v,0)+1
        for v,n in cnt.items():
            if n>=R*0.6 and n<R:
                v_runs.append((c,v))
    # choose stripe
    stripe_type = None
    if h_runs and (not v_runs or len(h_runs)>len(v_runs)):
        stripe_type='h'
        stripe_rows = sorted({r for r,_ in h_runs})
        sr0, sr1 = stripe_rows[0], stripe_rows[-1]
    else:
        stripe_type='v'
        stripe_cols = sorted({c for c,_ in v_runs})
        sc0, sc1 = stripe_cols[0], stripe_cols[-1]
    # 4) compute crop
    if stripe_type=='h':
        top = cluster_bot+1
        bot = sr0-1
        left = cluster_left
        right = cluster_right
        # expand left/right until cluster bounds
        # if cluster small, take wider by pattern width
        width = right-left+1
        # if too narrow, center on cluster
        if width< C//3:
            left = 0
            right = C-1
        out = [row[left:right+1] for row in grid[top:bot+1]]
    else:
        left = sc1+1
        right = cluster_left-1 if clusters else cluster_left-1
        top = cluster_top
        bot = cluster_bot
        height = bot-top+1
        if height< R//3:
            top = 0
            bot = R-1
        out = [row[left:sc0] for row in grid]
        # then crop rows
        out = out[top:bot+1]
    return out