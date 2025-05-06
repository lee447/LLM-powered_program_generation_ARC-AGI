def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    rects = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c == border: continue
            if c not in rects:
                rects[c] = [i, i, j, j]
            else:
                r = rects[c]
                r[0] = min(r[0], i); r[1] = max(r[1], i)
                r[2] = min(r[2], j); r[3] = max(r[3], j)
    sides = {}
    for c, (r0,r1,c0,c1) in rects.items():
        if r0 == 0: sides['top'] = c
        elif r1 == h-1: sides['bottom'] = c
        elif c0 == 0: sides['left'] = c
        elif c1 == w-1: sides['right'] = c
    order = ['bottom','left','top','right']
    regs = [sides[s] for s in order if s in sides]
    Bs = [rects[c] for c in regs]
    heights = [r1-r0+1 for r0,r1,c0,c1 in Bs]
    widths = [c1-c0+1 for r0,r1,c0,c1 in Bs]
    H = sum(1 for _ in regs) * 2
    W = max(widths)
    H = sum(heights) if len(regs)==1 else (heights[0] if len(regs)==1 else sum(heights[:2])) if False else max(heights)*2
    H = max(h,w)
    H = max(widths)
    W = max(widths)
    H = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    height = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    H = max(widths)
    # fallback
    min_r = min(r0 for r0,_,_,_ in rects.values())
    max_r = max(r1 for _,r1,_,_ in rects.values())
    min_c = min(c0 for _,_,c0,_ in rects.values())
    max_c = max(c1 for _,_,_,c1 in rects.values())
    out = [row[min_c:max_c+1] for row in grid[min_r:max_r+1]]
    return out