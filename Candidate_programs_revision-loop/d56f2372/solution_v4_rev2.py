import sys
sys.setrecursionlimit(10000)
def solve(grid):
    h=len(grid); w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    candidates=[]
    order=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not seen[i][j]:
                color=grid[i][j]
                stack=[(i,j)]; pts=[]; seen[i][j]=True
                while stack:
                    y,x=stack.pop(); pts.append((y,x))
                    for dy,dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==color:
                            seen[ny][nx]=True; stack.append((ny,nx))
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                r0,r1,c0,c1=min(rs),max(rs),min(cs),max(cs)
                height=r1-r0+1; width=c1-c0+1
                if height<2 or width<2: continue
                sub=[[0]*width for _ in range(height)]
                for y,x in pts: sub[y-r0][x-c0]=color
                ok=True
                for row in sub:
                    if row!=row[::-1]: ok=False; break
                if not ok: continue
                if sub==sub[::-1]: continue
                patterns={tuple(row) for row in sub}
                candidates.append((len(patterns),order,sub))
                order+=1
    if not candidates: return []
    best=min(candidates,key=lambda x:(-x[0],x[1]))
    return best[2]