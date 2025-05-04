def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    freq={}
    for r in range(h):
        for c in range(w):
            freq[grid[r][c]]=freq.get(grid[r][c],0)+1
    bg=max(freq,key=lambda x:freq[x])
    template_color=max((c for c in freq if c!=bg),key=lambda x:freq[x])
    pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==template_color]
    minr=min(r for r,c in pts);minc=min(c for r,c in pts)
    template=[(r-minr,c-minc) for r,c in pts]
    templ_set=set(template)
    for color in set(freq)-{bg,template_color}:
        pts_c=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==color]
        if not pts_c: continue
        pr,pc=pts_c[0]
        for tr,tc in template:
            dr=pr-tr;dc=pc-tc
            if all((r-dr,c-dc) in templ_set for r,c in pts_c):
                break
        for r,c in pts_c:
            out[r][c]=bg
        for tr,tc in template:
            rr=tr+dr;cc=tc+dc
            if 0<=rr<h and 0<=cc<w:
                out[rr][cc]=color
    return out