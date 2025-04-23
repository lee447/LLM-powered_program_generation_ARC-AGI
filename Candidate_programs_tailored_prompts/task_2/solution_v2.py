def solve(grid):
    h, w = len(grid), len(grid[0])
    ac = {8,9}
    cr = [r for r in range(h) for c in range(w) if grid[r][c] in ac]
    cc = [c for r in range(h) for c in range(w) if grid[r][c] in ac]
    top, bottom = min(cr), max(cr)
    left, right = min(cc), max(cc)
    cluster_colors = {6,7}
    counts = {}
    # left
    if left > 0:
        counts['left'] = sum(1 for r in range(top, bottom+1) if grid[r][left-1] in cluster_colors)
    else:
        counts['left'] = -1
    # right
    if right < w-1:
        counts['right'] = sum(1 for r in range(top, bottom+1) if grid[r][right+1] in cluster_colors)
    else:
        counts['right'] = -1
    # top
    if top > 0:
        counts['top'] = sum(1 for c in range(left, right+1) if grid[top-1][c] in cluster_colors)
    else:
        counts['top'] = -1
    # bottom
    if bottom < h-1:
        counts['bottom'] = sum(1 for c in range(left, right+1) if grid[bottom+1][c] in cluster_colors)
    else:
        counts['bottom'] = -1
    # side with cluster
    cluster_side = max(counts, key=lambda s: counts[s])
    opp = {'left':'right','right':'left','top':'bottom','bottom':'top'}[cluster_side]
    d = {'left':(0,-1),'right':(0,1),'top':(-1,0),'bottom':(1,0)}[opp]
    dr, dc = d
    H, W = bottom-top+1, right-left+1
    out = [[grid[top+i+dr][left+j+dc] for j in range(W)] for i in range(H)]
    return out