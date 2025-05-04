def solve(grid):
    h=len(grid); w=len(grid[0])
    twos=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==2]
    s2=set(twos)
    for i,j in twos:
        if (i-1,j) in s2 and (i+1,j) in s2 and (i,j-1) in s2 and (i,j+1) in s2:
            ci, cj = i, j
            break
    else:
        is_[0]=min(i for i,_ in twos); im=max(i for i,_ in twos)
        js=[j for _,j in twos]; js0=min(js); jm=max(js)
        ci=(is_[0]+im)//2; cj=(js0+jm)//2
    out=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==2:
                out[i][j]=2
            else:
                di=abs(i-ci); dj=abs(j-cj); d=max(di,dj)
                if di==dj and di>0:
                    out[i][j]=1
                elif (i==ci or j==cj) and d>0:
                    if d<2:
                        out[i][j]=2
                    else:
                        out[i][j]=8 if (d-2)%3<2 else 4
    return out