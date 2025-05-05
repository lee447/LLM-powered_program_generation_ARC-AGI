def solve(grid):
    h=len(grid); w=len(grid[0])
    grey_rows=[any(cell==5 for cell in row) for row in grid]
    stripes=[]; cur=[]
    for i,gr in enumerate(grey_rows):
        if gr:
            cur.append(i)
        else:
            if cur:
                stripes.append(cur)
                cur=[]
    if cur: stripes.append(cur)
    stripes=[g for g in stripes if len(g)>=2]
    stripes=[g[:2] for g in stripes]
    first=stripes[0]; r0=first[0]; cpos=[]
    for c in range(w-1):
        cnt=sum(grid[r0+dr][c+dc]!=0 for dr in (0,1) for dc in (0,1))
        if cnt>=3: cpos.append(c)
    b=len(cpos)
    out_w=b*2+(b-1)*1
    blocks=[]
    for stripe in stripes:
        r0=stripe[0]
        cols=[]
        for c in cpos:
            color=None
            for dr in (0,1):
                for dc in (0,1):
                    v=grid[r0+dr][c+dc]
                    if v!=5 and v!=0:
                        color=v
            cols.append(color)
        blocks.append(cols)
    s=len(blocks)
    out_h=s*2+(s-1)*1
    out=[[0]*out_w for _ in range(out_h)]
    for i,cols in enumerate(blocks):
        base_row=i*3
        for j,color in enumerate(cols):
            if color is None: continue
            base_col=j*3
            out[base_row][base_col]=color
            out[base_row][base_col+1]=color
            out[base_row+1][base_col]=color
            out[base_row+1][base_col+1]=color
    return out