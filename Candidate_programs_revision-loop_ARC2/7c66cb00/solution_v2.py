def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=grid[0][0]
    blank=[all(c==bg for c in row) for row in grid]
    stripes=[]
    i=0
    while i<h:
        if blank[i]:
            i+=1
            continue
        j=i
        while j<h and not blank[j]:
            j+=1
        stripes.append((i,j))
        i=j
    # find shapes in first stripe
    y0,y1=stripes[0]
    visited=[[False]*w for _ in range(h)]
    shapes=[]
    for y in range(y0,y1):
        for x in range(w):
            if not visited[y][x] and grid[y][x]!=bg:
                col0=grid[y][x]
                stack=[(y,x)]; comp=[]
                visited[y][x]=True
                while stack:
                    yy,xx=stack.pop()
                    comp.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]!=bg:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                if len(comp)>1:
                    ys=[p[0] for p in comp]; xs=[p[1] for p in comp]
                    sy0,sy1=min(ys),max(ys)
                    sx0,sx1=min(xs),max(xs)
                    pixels=[(yy-sy0, xx-sx0, grid[yy][xx]) for yy,xx in comp]
                    shapes.append((sy1-sy0+1, sx1-sx0+1, sy0, sx0, pixels))
    shapes.sort(key=lambda s: s[0]*s[1], reverse=True)
    out=[row[:] for row in grid]
    for idx, (y0,y1) in enumerate(stripes[1:],1):
        if idx>len(shapes): break
        sh_h,sh_w, sy0, sx0, pixels = shapes[idx-1]
        # find stripe bbox cols
        cols=[x for x in range(w) if any(grid[y][x]!=bg for y in range(y0,y1))]
        if not cols: continue
        cx0, cx1=min(cols), max(cols)
        # stripe colors
        interior_counts={}
        for y in range(y0+1,y1-1):
            for x in range(cx0+1,cx1):
                if grid[y][x]!=bg:
                    interior_counts[grid[y][x]]=interior_counts.get(grid[y][x],0)+1
        if interior_counts:
            sc_int=max(interior_counts, key=interior_counts.get)
        else:
            sc_int=bg
        border_counts={}
        for x in range(cx0, cx1+1):
            for y in (y0,y1-1):
                c=grid[y][x]
                if c!=bg: border_counts[c]=border_counts.get(c,0)+1
        for y in range(y0,y1):
            for x in (cx0, cx1):
                c=grid[y][x]
                if c!=bg: border_counts[c]=border_counts.get(c,0)+1
        if border_counts:
            sc_bor=max(border_counts, key=border_counts.get)
        else:
            sc_bor=bg
        # shape color mapping
        cnts={}
        for _,_,c in pixels: cnts[c]=cnts.get(c,0)+1
        cols_sh=list(cnts.keys())
        if len(cols_sh)==1:
            bor=None; interior=cols_sh[0]
        else:
            a,b=cols_sh
            if cnts[a]>cnts[b]:
                bor=a; interior=b
            else:
                bor=b; interior=a
        # position
        th=y1-y0; tw=cx1-cx0+1
        oy=y0+(th-sh_h)//2; ox=cx0+(tw-sh_w)//2
        for dy,dx,c in pixels:
            ny,nx=oy+dy, ox+dx
            if 0<=ny<h and 0<=nx<w:
                if len(cols_sh)==1:
                    out[ny][nx]=sc_int
                else:
                    out[ny][nx]= sc_bor if c==bor else sc_int
    return out