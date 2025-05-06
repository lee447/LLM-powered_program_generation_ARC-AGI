def solve(grid):
    h=len(grid); w=len(grid[0])
    sep_rows=[i for i,row in enumerate(grid) if len(set(row))==1 and row[0]!=0]
    sep_cols=[j for j in range(w) if len({grid[i][j] for i in range(h)})==1 and grid[0][j]!=0]
    tile=sep_rows[0]+1
    interior=tile-1
    groups={}
    for br in range((h+tile-1)//tile):
        y0=br*tile
        if y0+interior>h-1: break
        for bc in range((w+tile-1)//tile):
            x0=bc*tile
            if x0+interior> w-1: break
            cell_offsets={}
            for dy in range(interior):
                for dx in range(interior):
                    v=grid[y0+dy][x0+dx]
                    if v!=0 and (y0+interior not in sep_rows or v!=grid[y0+interior][x0+dx]) and (x0+interior not in sep_cols or v!=grid[y0+dy][x0+interior]):
                        cell_offsets.setdefault(v,[]).append((dy,dx))
            for c,offs in cell_offsets.items():
                if offs:
                    groups.setdefault(c,[]).append((br,bc,offs))
    out=[row[:] for row in grid]
    for c,blks in groups.items():
        rs=[b[0] for b in blks]
        cs=[b[1] for b in blks]
        rmin,rmax=min(rs),max(rs)
        cmin,cmax=min(cs),max(cs)
        tmpl = None
        for br,bc,offs in blks:
            if br==rmin and bc==cmin:
                tmpl=offs; break
        if tmpl is None: tmpl=blks[0][2]
        for br in range(rmin,rmax+1):
            for bc in range(cmin,cmax+1):
                if not any(br==rb and bc==cb for rb,cb,_ in blks):
                    y0=br*tile; x0=bc*tile
                    for dy,dx in tmpl:
                        ydy = dy if br<=rmin else interior-1-dy
                        xdx = dx if bc<=cmin else interior-1-dx
                        out[y0+ydy][x0+xdx]=c
    return out