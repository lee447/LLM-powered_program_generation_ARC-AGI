def solve(grid):
    h=len(grid); w=len(grid[0])
    res=[row[:] for row in grid]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    def inb(x,y): return 0<=x<h and 0<=y<w
    for color in range(2,10):
        pts=[(i,j) for i in range(h) for j in range(w) if res[i][j]==color]
        if not pts or len(pts)>=4: continue
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        cx=(min(xs)+max(xs))/2; cy=(min(ys)+max(ys))/2
        new=set()
        for x,y in pts:
            for k in (1,2,3):
                # rotate k*90
                if k==1:
                    xn=cx-(y-cy); yn=cy+(x-cx)
                elif k==2:
                    xn=2*cx-x; yn=2*cy-y
                else:
                    xn=cx+(y-cy); yn=cy-(x-cx)
                if abs(xn-round(xn))<1e-6 and abs(yn-round(yn))<1e-6:
                    xi,yi=int(round(xn)),int(round(yn))
                    if inb(xi,yi) and res[xi][yi]==1:
                        new.add((xi,yi))
        for x,y in new:
            res[x][y]=color
        pts=[(i,j) for i in range(h) for j in range(w) if res[i][j]==color]
    changed=True
    while changed:
        changed=False
        for x in range(1,h-1):
            for y in range(1,w-1):
                if res[x][y]==1:
                    for color in range(2,10):
                        if res[x-1][y]==color and res[x+1][y]==color:
                            res[x][y]=color; changed=True
                        if res[x][y-1]==color and res[x][y+1]==color:
                            res[x][y]=color; changed=True
    return res