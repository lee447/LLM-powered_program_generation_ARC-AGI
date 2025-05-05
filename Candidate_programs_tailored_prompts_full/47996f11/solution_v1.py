def solve(grid):
    H=len(grid); W=len(grid[0])
    # find frame rows
    row7counts=[row.count(7) for row in grid]
    max7=max(row7counts)
    frame_rows=[i for i,c in enumerate(row7counts) if c>=max7-1]
    frame_top=frame_rows[0]; frame_bottom=frame_rows[-1]
    # find frame cols from top
    row=grid[frame_top]
    best_seg=[]
    segs=[]
    i=0
    while i<W:
        if row[i]==7:
            j=i
            while j<W and row[j]==7: j+=1
            segs.append((i,j-1))
            i=j
        else: i+=1
    # pick largest
    segs.sort(key=lambda x: x[1]-x[0], reverse=True)
    frame_left,frame_right=segs[0]
    # find pink cols (6)
    col6=[sum(1 for y in range(H) if grid[y][x]==6) for x in range(W)]
    pink_cols=[x for x,c in enumerate(col6) if c>H//4]
    pink_cols.sort()
    if not pink_cols: return grid
    pink_start,pink_end=pink_cols[0],pink_cols[-1]
    interior_x0,interior_x1=frame_left+1,frame_right-1
    pattern_colors={1,2,3,4}
    out=[row[:] for row in grid]
    for y in range(frame_top+1,frame_bottom):
        # find segments of pattern colors in interior
        segs=[]
        x=interior_x0
        while x<=interior_x1:
            if grid[y][x] in pattern_colors:
                a=x
                while x<=interior_x1 and grid[y][x] in pattern_colors: x+=1
                segs.append((a,x-1))
            else: x+=1
        for a,b in segs:
            if b-a<=(pink_end-pink_start+1) and (a==interior_x0 or b==interior_x1):
                vals=[grid[y][i] for i in range(a,b+1)]
                vals=vals[::-1]
                for i,v in enumerate(vals):
                    if pink_start+i<=pink_end:
                        out[y][pink_start+i]=v
                break
    return out