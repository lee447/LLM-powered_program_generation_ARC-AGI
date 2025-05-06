def solve(grid):
    n=len(grid)
    m=n//3
    blocks=[]
    for bi in range(3):
        for bj in range(3):
            block=[row[bj*m:(bj+1)*m] for row in grid[bi*m:(bi+1)*m]]
            blocks.append(block)
    cnt={}
    for b in blocks:
        key=tuple(tuple(r) for r in b)
        cnt[key]=cnt.get(key,0)+1
    for b in blocks:
        key=tuple(tuple(r) for r in b)
        if cnt[key]==1:
            uniq=b
            break
    freq={}
    for row in uniq:
        for c in row:
            freq[c]=freq.get(c,0)+1
    bg=max(freq, key=lambda k:freq[k])
    R=len(uniq); C=len(uniq[0])
    rmin,Rmax=R, -1
    cmin,Cmax=C, -1
    for i in range(R):
        for j in range(C):
            if uniq[i][j]!=bg:
                rmin=min(rmin,i); Rmax=max(Rmax,i)
                cmin=min(cmin,j); Cmax=max(Cmax,j)
    if Rmax<0:
        return []
    return [uniq[i][cmin:Cmax+1] for i in range(rmin,Rmax+1)]