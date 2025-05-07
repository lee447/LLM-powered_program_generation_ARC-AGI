def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    dirs8 = [(dr,dc) for dr in (-1,0,1) for dc in (-1,0,1)]
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                q=[(i,j)]
                seen[i][j]=True
                comp={(i,j)}
                for r,c in q:
                    for dr,dc in dirs4:
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and not seen[rr][cc] and grid[rr][cc]==1:
                            seen[rr][cc]=True
                            q.append((rr,cc))
                            comp.add((rr,cc))
                clusters.append(comp)
    clusters.sort(key=len, reverse=True)
    to_paint = clusters[:2]
    out = [[4]*w for _ in range(h)]
    for comp in to_paint:
        prev = set(comp)
        for step,color in [(1,2),(2,8),(3,6)]:
            d = set(prev)
            for r,c in prev:
                for dr,dc in dirs8:
                    rr,cc = r+dr, c+dc
                    if 0<=rr<h and 0<=cc<w:
                        d.add((rr,cc))
            ring = d - prev
            for r,c in ring:
                out[r][c] = color
            prev = d
        for r,c in comp:
            out[r][c] = 1
    return out