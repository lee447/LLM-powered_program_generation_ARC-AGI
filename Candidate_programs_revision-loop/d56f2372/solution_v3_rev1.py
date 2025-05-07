import sys
sys.setrecursionlimit(10000)
def solve(grid):
    h=len(grid); w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    def flood(r,c,color):
        stack=[(r,c)]; seen[r][c]=True; pts=[]
        while stack:
            y,x=stack.pop(); pts.append((y,x))
            for dy,dx in dirs:
                ny, nx = y+dy, x+dx
                if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==color:
                    seen[ny][nx]=True
                    stack.append((ny,nx))
        return pts
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not seen[i][j]:
                color=grid[i][j]
                pts=flood(i,j,color)
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                sub=[[0]*(maxc-minc+1) for _ in range(r1-r0+1)]
                for y,x in pts:
                    sub[y-r0][x-minc]=color
                ok=True
                for row in sub:
                    if row!=row[::-1]:
                        ok=False
                        break
                if ok:
                    return sub
    return []
import json
if __name__=='__main__':
    data=sys.stdin.read().strip()
    grid=json.loads(data)
    res=solve(grid)
    print(json.dumps(res))