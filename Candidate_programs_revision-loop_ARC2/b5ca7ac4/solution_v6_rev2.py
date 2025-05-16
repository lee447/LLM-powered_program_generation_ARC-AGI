import math
from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    vis=[[False]*w for _ in grid]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not vis[i][j]:
                c=grid[i][j]
                q=deque([(i,j)])
                vis[i][j]=True
                cells=[]
                while q:
                    y,x=q.popleft()
                    cells.append((y,x))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==c:
                            vis[ny][nx]=True
                            q.append((ny,nx))
                ys=[y for y,_ in cells]; xs=[x for _,x in cells]
                miny,maxy,minx,maxx=min(ys),max(ys),min(xs),max(xs)
                H,W=maxy-miny+1,maxx-minx+1
                rel=set((y-miny,x-minx) for y,x in cells)
                comps.append((miny,minx,H,W,c,rel))
    rings=[]; squares=[]
    for y,x,H,W,c,rel in comps:
        if H==W and len(rel)==4*H-4: rings.append((y,x,H,c,rel))
        if H==W and len(rel)==H*H: squares.append((y,x,H,c,rel))
    pairs=[]
    for ry,rx,L,colr,relr in rings:
        for sy,sx,LS,cols,rels in squares:
            if LS+2==L and ry<sy and ry+L>sy+LS and rx<sx and rx+L>sx+LS:
                pairs.append((ry,rx,L,colr,relr,sy,sx,cols,rels))
                break
    N=len(pairs)
    mid_y,mid_x=(h-1)/2,(w-1)/2
    def center(pair):
        ry,rx,L=pair[0],pair[1],pair[2]
        return ry+(L-1)/2,rx+(L-1)/2
    def ang(pair):
        cy,cx=center(pair)
        return (math.atan2(mid_y-cy, cx-mid_x)-math.pi/2)%(2*math.pi)
    pairs.sort(key=ang)
    out=[[0]*w for _ in range(h)]
    for i,(ry,rx,L,colr,relr,sy,sx,cols,rels) in enumerate(pairs):
        theta=math.pi/2-2*math.pi*i/N
        R=(min(h,w)-L)/2
        cy=mid_y-math.sin(theta)*R
        cx=mid_x+math.cos(theta)*R
        r0=int(round(cy-(L-1)/2))
        c0=int(round(cx-(L-1)/2))
        path=[]
        for dx in range(L): path.append((0,dx))
        for dy in range(1,L): path.append((dy,L-1))
        for dx in range(L-2,-1,-1): path.append((L-1,dx))
        for dy in range(L-2,0,-1): path.append((dy,0))
        pts=sorted(relr)
        for (dy,dx),(oy,ox) in zip(path,pts):
            out[r0+dy][c0+dx]=colr
        for dy,dx in rels:
            out[r0+1+dy][c0+1+dx]=cols
    return out