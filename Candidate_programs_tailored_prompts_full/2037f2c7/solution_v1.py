def solve(grid):
    h, w = len(grid), len(grid[0])
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not coords:
        return []
    cols = sorted({c for _, c in coords})
    split_idx = 0
    max_gap = 0
    for i in range(len(cols) - 1):
        gap = cols[i+1] - cols[i]
        if gap > max_gap:
            max_gap, split_idx = gap, i
    if max_gap > 1:
        left_cols = set(cols[:split_idx+1])
    else:
        left_cols = set(cols)
    cluster = [(r, c) for (r, c) in coords if c in left_cols]
    rmin = min(r for r, _ in cluster)
    rmax = max(r for r, _ in cluster)
    cmin = min(c for _, c in cluster)
    cmax = max(c for _, c in cluster)
    H, W = rmax - rmin + 1, cmax - cmin + 1
    sub = [[grid[rmin + r][cmin + c] for c in range(W)] for r in range(H)]
    bpoints = []
    for r in range(H):
        for c in range(W):
            if sub[r][c] != 0:
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=H or nc<0 or nc>=W or sub[nr][nc] == 0:
                        bpoints.append((r,c))
                        break
    sel = set()
    # horizontal runs
    from collections import defaultdict
    byrow = defaultdict(list)
    for r,c in bpoints:
        byrow[r].append(c)
    for r, clist in byrow.items():
        clist = sorted(set(clist))
        run = [clist[0]]
        for x in clist[1:]:
            if x == run[-1] + 1:
                run.append(x)
            else:
                if len(run) >= 2:
                    sel.add((r, run[0])); sel.add((r, run[-1]))
                else:
                    sel.add((r, run[0]))
                run = [x]
        if run:
            if len(run) >= 2:
                sel.add((r, run[0])); sel.add((r, run[-1]))
            else:
                sel.add((r, run[0]))
    # vertical runs
    bycol = defaultdict(list)
    for r,c in bpoints:
        bycol[c].append(r)
    for c, rlist in bycol.items():
        rlist = sorted(set(rlist))
        run = [rlist[0]]
        for x in rlist[1:]:
            if x == run[-1] + 1:
                run.append(x)
            else:
                L = len(run)
                if L == 1:
                    sel.add((run[0], c))
                elif L == 2:
                    sel.add((run[0], c)); sel.add((run[1], c))
                else:
                    sel.add((run[0], c)); sel.add((run[-1], c)); sel.add((run[L//2], c))
                run = [x]
        if run:
            L = len(run)
            if L == 1:
                sel.add((run[0], c))
            elif L == 2:
                sel.add((run[0], c)); sel.add((run[1], c))
            else:
                sel.add((run[0], c)); sel.add((run[-1], c)); sel.add((run[L//2], c))
    rows_used = sorted({r for r, _ in sel})
    out_h = len(rows_used)
    row_map = {r:i for i,r in enumerate(rows_used)}
    out = [[0]*W for _ in range(out_h)]
    for r,c in sel:
        out[row_map[r]][c] = 8
    return out