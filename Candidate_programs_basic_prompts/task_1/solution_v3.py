def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    col_nz=[sum(1 for i in range(h) if grid[i][j]!=0) for j in range(w)]
    colmask=[cnt>=3 for cnt in col_nz]
    colsegs=[]
    j=0
    while j<w:
        if colmask[j]:
            st=j
            while j<w and colmask[j]:
                j+=1
            colsegs.append((st,j))
        else:
            j+=1
    row_nz=[sum(1 for j in range(w) if grid[i][j]!=0) for i in range(h)]
    rowmask=[cnt>=3 for cnt in row_nz]
    rowsegs=[]
    i=0
    while i<h:
        if rowmask[i]:
            st=i
            while i<h and rowmask[i]:
                i+=1
            rowsegs.append((st,i))
        else:
            i+=1
    for r0,r1 in rowsegs:
        for c0,c1 in colsegs:
            found=False
            for i in range(r0,r1):
                for j in range(c0,c1):
                    if grid[i][j]!=0:
                        found=True;break
                if found:break
            if not found:continue
            freq={}
            for i in range(r0,r1):
                pat=tuple(grid[i][j] for j in range(c0,c1))
                freq[pat]=freq.get(pat,0)+1
            best=max(freq.items(),key=lambda x:x[1])[0]
            for i in range(r0,r1):
                for k,j in enumerate(range(c0,c1)):
                    out[i][j]=best[k]
    return out