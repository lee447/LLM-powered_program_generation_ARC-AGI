def solve(grid):
    H=len(grid); W=len(grid[0])
    stripe_rows=[r for r in range(H) if len(set(grid[r]))==1]
    anchor_color=grid[stripe_rows[0]][0]
    stripe_rows=[r for r in stripe_rows if grid[r][0]==anchor_color]
    stripe_cols=[c for c in range(W) if all(grid[r][c]==anchor_color for r in range(H))]
    counts={}
    for r in range(H-1):
        for c in range(W-1):
            v=grid[r][c]
            if v==anchor_color: continue
            if grid[r][c+1]==v and grid[r+1][c]==v and grid[r+1][c+1]==v:
                if r in stripe_rows or r+1 in stripe_rows or c in stripe_cols or c+1 in stripe_cols:
                    continue
                counts[v]=counts.get(v,0)+1
    if not counts: return []
    items=sorted(counts.items(), key=lambda x:x[1])
    m=max(counts.values())
    return [[v]*cnt+[0]*(m-cnt) for v,cnt in items]