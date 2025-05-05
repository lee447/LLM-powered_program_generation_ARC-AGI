def solve(grid):
    n=len(grid)
    c_in=n//2
    c_out=c_in+1
    center_out=c_out//2
    R_out=center_out
    res=[[0]*c_out for _ in range(c_out)]
    for i in range(n):
        for j in range(n):
            v=grid[i][j]
            if v==0: continue
            dx=i-c_in
            dy=j-c_in
            if dx==0 and dy==0:
                i2,j2=center_out,center_out
            else:
                adx,ady=abs(dx),abs(dy)
                if adx==ady:
                    if adx==c_in:
                        dx2=(dx//adx)*R_out
                        dy2=(dy//ady)*R_out
                    else:
                        if dx*dy>0:
                            dx2=(dx//adx)*R_out
                            dy2=0
                        else:
                            dx2=0
                            dy2=(dy//ady)*R_out
                    i2=center_out+dx2
                    j2=center_out+dy2
                else:
                    continue
            res[i2][j2]=v
    return res