def solve(grid):
    h=len(grid); w=len(grid[0])
    bar_row = max(i for i,row in enumerate(grid) if row.count(row[0])==w and row[0]!=0)
    bar_color = grid[bar_row][0]
    shapes=[]
    for c in set(val for row in grid for val in row):
        if c==0 or c==bar_color: continue
        coords=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==c]
        rs=[i for i,j in coords]; cs=[j for i,j in coords]
        r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
        arr=[row[minc:maxc+1] for row in grid[r0:r1+1]]
        shapes.append((c,arr,len(coords),r0,minc))
    shapes.sort(key=lambda x:x[2])
    region_h=2; start_row=bar_row-region_h
    new=[[0]*w for _ in range(h)]
    new[bar_row]=grid[bar_row].copy()
    if len(shapes)==1:
        c,arr,_,r0,minc=shapes[0]
        sh,sw=len(arr),len(arr[0])
        if sh!=region_h:
            arr=[[arr[sh-1-j][i] for j in range(sh)] for i in range(sw)]
            sh,sw=sw,sh
        x=max(minc-1,0)
        for dy in range(region_h):
            for dx in range(sw):
                if arr[dy][dx]!=0:
                    new[start_row+dy][x+dx]=arr[dy][dx]
    else:
        ns=len(shapes)
        ws=[]
        rots=[]
        for c,arr,_,r0,minc in shapes:
            sh,sw=len(arr),len(arr[0])
            if sh!=region_h:
                arr=[[arr[sh-1-j][i] for j in range(sh)] for i in range(sw)]
                sh,sw=sw,sh
            rots.append((c,arr))
            ws.append(sw)
        total_w=sum(ws)
        gaps=ns+1; free=w-total_w
        fg=free//gaps; rem=free%gaps
        gap_sizes=[fg + (1 if i>=gaps-rem else 0) for i in range(gaps)]
        x=gap_sizes[0]
        for i,(c,arr) in enumerate(rots):
            sh,sw=len(arr),len(arr[0])
            for dy in range(region_h):
                for dx in range(sw):
                    if arr[dy][dx]!=0:
                        new[start_row+dy][x+dx]=arr[dy][dx]
            x+=sw+gap_sizes[i+1]
    return new