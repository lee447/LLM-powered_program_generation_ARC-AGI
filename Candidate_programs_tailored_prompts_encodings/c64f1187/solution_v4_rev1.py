def solve(grid):
    h=len(grid); w=len(grid[0])
    shape_rows=[i for i in range(h) if any(grid[i][j]==1 for j in range(w))]
    top=min(shape_rows); bottom=max(shape_rows)
    th=bottom-top+1
    color_row=top-1
    maskcols=[any(grid[r][c]==1 for r in range(top,bottom+1)) for c in range(w)]
    segments=[]; c=0
    while c<w:
        if maskcols[c]:
            seg=[]
            while c<w and maskcols[c]:
                seg.append(c); c+=1
            segments.append(seg)
        else:
            c+=1
    templates=[]; tcols=[]
    for seg in segments:
        tm=[[1 if grid[top+dr][c]==1 else 0 for c in seg] for dr in range(th)]
        templates.append(tm)
        color=None
        for c in seg:
            v=grid[color_row][c]
            if v not in (0,1):
                color=v; break
        if color is None:
            for c in seg:
                if c>0:
                    v=grid[color_row][c-1]
                    if v not in (0,1,5):
                        color=v; break
        tcols.append(color)
    stripes=[]; in_s=False
    for i in range(h):
        if any(grid[i][j]==5 for j in range(w)):
            if not in_s:
                in_s=True; stripes.append([])
            stripes[-1].append(i)
        else:
            in_s=False
    r0=stripes[0][0]
    tw=len(segments[0])
    cpos=[c for c in range(w-tw+1) if all(grid[r0][c+dc]==5 for dc in range(tw))]
    ns=len(stripes); nc=len(cpos)
    out_h=ns*th+(ns-1); out_w=nc*tw+(nc-1)
    out=[[0]*out_w for _ in range(out_h)]
    for i,stripe in enumerate(stripes):
        br=i*(th+1)
        for j,c in enumerate(cpos):
            color=None
            for r in stripe:
                for dc in range(tw):
                    v=grid[r][c+dc]
                    if v not in (0,5):
                        color=v
            if color is None: continue
            ti=tcols.index(color)
            tm=templates[ti]
            for dr in range(th):
                for dc in range(tw):
                    if tm[dr][dc]:
                        out[br+dr][j*(tw+1)+dc]=color
    return out