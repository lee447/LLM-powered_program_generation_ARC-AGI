def solve(grid):
    h, w = len(grid), len(grid[0])
    stripes = [c for c,v in enumerate(grid[0]) if v and v!=8][:3]
    colors = [grid[0][c] for c in stripes]
    pat = [4,2,4]
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        runs = []
        c = 0
        while c<w:
            if grid[r][c]==8:
                s=c
                while c<w and grid[r][c]==8: c+=1
                runs.append((s,c))
            else:
                c+=1
        for i,(s,e) in enumerate(runs):
            L = e-s
            mid = (s+e-1)/2
            left = (mid < w/2)
            seg = colors if left else colors
            rem = L
            if left:
                x = s
                for col,width in zip(seg,pat):
                    if rem<=0: break
                    t=min(width,rem)
                    for k in range(t): out[r][x+k]=col
                    x+=t; rem-=t
            else:
                x = e
                for col,width in zip(reversed(seg),reversed(pat)):
                    if rem<=0: break
                    t=min(width,rem)
                    for k in range(t): out[r][x-1-k]=col
                    x-=t; rem-=t
    return out