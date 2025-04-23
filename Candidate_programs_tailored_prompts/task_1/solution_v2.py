def solve(grid):
    H=len(grid);W=len(grid[0])
    out=[[0]*W for _ in range(H)]
    vals={v for row in grid for v in row}
    if 6 in vals:
        grey_rows=[]
        for r in range(H):
            c=0
            while c<W:
                if grid[r][c]==6:
                    start=c
                    while c<W and grid[r][c]==6: c+=1
                    if c-start>=6: grey_rows.append((r,start))
                else: c+=1
        for r,start in grey_rows:
            for c in range(start,start+6):
                out[r][c]=6
            for dr in range(1,5):
                for c in range(start,start+6):
                    v=grid[r+dr][c]
                    if v in (8,3): out[r+dr][c]=v
    elif 8 in vals:
        band_rows=[]
        for r in range(H):
            c=0
            while c<W:
                if grid[r][c]==8:
                    s=c
                    while c<W and grid[r][c]==8: c+=1
                    if c-s>=5: band_rows.append((r,s))
                else: c+=1
        if band_rows:
            r8,_=band_rows[0]
            r0=r8-4
            c_offs=[s for r,s in band_rows if r==r8]
            for base in range(r0,H,6):
                for dr in range(6):
                    r=base+dr
                    if r<0 or r>=H: continue
                    if dr<4:
                        for s in c_offs:
                            v=grid[r][s]
                            w=0
                            while s+w<W and grid[r][s+w]==v: w+=1
                            for k in range(w): out[r][s+k]=v
                    elif dr==4:
                        for s in c_offs:
                            w=0
                            while s+w<W and grid[r][s+w]==8: w+=1
                            for k in range(w): out[r][s+k]=8
    else:
        r0=None; runs0=[]
        for i in range(H-3):
            c=0
            while c<W:
                if grid[i][c]!=0:
                    s=c
                    while c<W and grid[i][c]!=0: c+=1
                    if c-s>=4:
                        runs0.append((s,c-s))
                else: c+=1
            if runs0:
                for s,w in runs0:
                    cnt=0
                    for k in range(w):
                        if grid[i+3][s+k]!=0: cnt+=1
                    if cnt>=4:
                        r0=i
                        break
            if r0 is not None: break
        if r0 is not None:
            runs=[]
            c=0
            rchk=r0+3
            while c<W:
                if grid[rchk][c]!=0:
                    s=c
                    while c<W and grid[rchk][c]!=0: c+=1
                    if c-s>=4: runs.append((s,min(4,c-s)))
                else: c+=1
            for base in range(r0,H,6):
                for dr in range(4):
                    r=base+dr
                    if r<0 or r>=H: continue
                    for s,w in runs:
                        for k in range(w):
                            v=grid[r][s+k]
                            if v!=0: out[r][s+k]=v
    return out