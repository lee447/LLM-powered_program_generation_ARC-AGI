def solve(grid):
    from collections import Counter, deque
    H, W = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=lambda c: cnt[c])
    centers = [ (y,x) for y in range(H) for x in range(W)
                if cnt[grid[y][x]]==2 and grid[y][x]!=bg ]
    clusters = []
    for cy,cx in centers:
        vis = set()
        q = deque([(cy,cx)])
        vis.add((cy,cx))
        while q:
            y,x = q.popleft()
            for dy in (-1,0,1):
                for dx in (-1,0,1):
                    ny, nx = y+dy, x+dx
                    if 0<=ny<H and 0<=nx<W and (ny,nx) not in vis and grid[ny][nx]!=bg:
                        vis.add((ny,nx))
                        q.append((ny,nx))
        ys = [y for y,x in vis]
        xs = [x for y,x in vis]
        y0, y1 = max(0,min(ys)-1), min(H-1,max(ys)+1)
        x0, x1 = max(0,min(xs)-1), min(W-1,max(xs)+1)
        block = [row[x0:x1+1] for row in grid[y0:y1+1]]
        border = block[1][0] if len(block)>1 and len(block[0])>0 else bg
        clusters.append((block, (y1-y0+1)*(x1-x0+1), border!=bg))
    clusters.sort(key=lambda x: (-x[1], -int(x[2])))
    if not clusters:
        return grid
    # compute total size
    blocks = [b for b,_,_ in clusters]
    spacer = [[bg]] * len(blocks)  # single-column spacer
    out_rows = len(blocks[0])
    for b in blocks:
        out_rows = max(out_rows, len(b))
    res = []
    for r in range(out_rows):
        row = []
        for i,b in enumerate(blocks):
            if r < len(b):
                row += b[r]
            else:
                row += [bg]*len(b[0])
            if i+1 < len(blocks):
                row += [bg]
        res.append(row)
    return res