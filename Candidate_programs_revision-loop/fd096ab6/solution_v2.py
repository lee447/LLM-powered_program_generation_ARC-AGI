def solve(grid):
    h=len(grid); w=len(grid[0])
    counts={}
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            counts[c]=counts.get(c,0)+1
    bg=max(counts, key=lambda k:counts[k])
    out=[row[:] for row in grid]
    for c,v in counts.items():
        if c==bg or v==5: continue
        pts=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==c]
        n_add=5-len(pts)
        cx=sum(i for i,_ in pts)/len(pts)
        cy=sum(j for _,j in pts)/len(pts)
        new=set()
        for i,j in pts:
            dx=i-cx; dy=j-cy
            ni, nj = cx+dy, cy-dx
            ri, rj = int(round(ni)), int(round(nj))
            if 0<=ri<h and 0<=rj<w and grid[ri][rj]!=c:
                new.add((ri,rj))
        new_list=list(new)
        new_list=new_list[:n_add]
        if len(new_list)<n_add:
            ci, cj = int(round(cx)), int(round(cy))
            if 0<=ci<h and 0<=cj<w and grid[ci][cj]!=c:
                new_list.append((ci,cj))
        for i,j in new_list:
            out[i][j]=c
    return out