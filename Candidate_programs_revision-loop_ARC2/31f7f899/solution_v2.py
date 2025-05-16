def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=grid[0][0]
    best_row=0; best_count=0; filler=None
    for i in range(h):
        cnt={}
        for c in grid[i]:
            if c!=bg:
                cnt[c]=cnt.get(c,0)+1
        for c,v in cnt.items():
            if v>best_count:
                best_count=v; best_row=i; filler=c
    center=best_row
    bars=[]
    for x in range(w):
        c=grid[center][x]
        if c!=bg and c!=filler:
            bars.append((x,c))
    bars.sort(key=lambda t:t[0])
    lengths=[]
    for x,c in bars:
        ymin=h; ymax=0
        for y in range(h):
            if grid[y][x]==c:
                ymin=min(ymin,y); ymax=max(ymax,y)
        lengths.append(ymax-ymin+1)
    new_lengths=sorted(lengths)
    out=[row[:] for row in grid]
    for i,(x,c) in enumerate(bars):
        nl=new_lengths[i]
        half=nl//2
        for y in range(h):
            out[y][x]=bg
        for y in range(center-half,center+half+1):
            if 0<=y<h:
                out[y][x]=c
    return out