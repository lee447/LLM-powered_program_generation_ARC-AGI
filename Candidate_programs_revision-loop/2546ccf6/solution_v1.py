def solve(grid):
    h=len(grid); w=len(grid[0])
    stripe_rows=[i for i in range(h) if len(set(grid[i]))==1 and grid[i][0]!=0]
    stripe_color=grid[stripe_rows[0]][0]
    stripe_cols=[j for j in range(w) if all(grid[i][j]==stripe_color for i in range(h))]
    block_row_ranges=[]
    last=0
    for r in stripe_rows:
        if r>last: block_row_ranges.append((last,r-1))
        last=r+1
    if last<h: block_row_ranges.append((last,h-1))
    block_col_ranges=[]
    last=0
    for c in stripe_cols:
        if c>last: block_col_ranges.append((last,c-1))
        last=c+1
    if last<w: block_col_ranges.append((last,w-1))
    from collections import defaultdict
    blocks_by_color=defaultdict(set)
    shape_coords={}
    for br,(r0,r1) in enumerate(block_row_ranges):
        for bc,(c0,c1) in enumerate(block_col_ranges):
            found=defaultdict(list)
            for i in range(r0,r1+1):
                for j in range(c0,c1+1):
                    v=grid[i][j]
                    if v!=0 and v!=stripe_color:
                        found[v].append((i-r0,j-c0))
            for v,coords in found.items():
                blocks_by_color[v].add((br,bc))
                shape_coords[(br,bc,v)]=coords
    res=[row[:] for row in grid]
    for v,blocks in blocks_by_color.items():
        rows=sorted({br for br,bc in blocks})
        cols=sorted({bc for br,bc in blocks})
        if len(rows)==2 and len(cols)==2 and len(blocks)==3:
            allpos={(r,c) for r in rows for c in cols}
            miss=list(allpos-blocks)[0]
            brm,bcm=miss
            src_br=rows[0]+rows[1]-brm
            src_bc=cols[0]+cols[1]-bcm
            coords=shape_coords[(src_br,src_bc,v)]
            r0,r1=block_row_ranges[brm]; c0,c1=block_col_ranges[bcm]
            bh=r1-r0+1; bw=c1-c0+1
            for (r_rel,c_rel) in coords:
                nr=r0+(bh-1-r_rel)
                nc=c0+(bw-1-c_rel)
                res[nr][nc]=v
    return res