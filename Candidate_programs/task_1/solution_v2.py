from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R=len(grid); C=len(grid[0])
    vis=[[False]*C for _ in range(R)]
    regions=[]
    for i in range(R):
        for j in range(C):
            if grid[i][j]!=0 and not vis[i][j]:
                stack=[(i,j)]; cells=[]
                vis[i][j]=True
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and grid[nr][nc]!=0 and not vis[nr][nc]:
                            vis[nr][nc]=True
                            stack.append((nr,nc))
                rmin=min(r for r,c in cells); rmax=max(r for r,c in cells)
                cmin=min(c for r,c in cells); cmax=max(c for r,c in cells)
                h=rmax-rmin+1; w=cmax-cmin+1
                if h*w==len(cells) and h*w>=5:
                    vals=[grid[r][c] for r,c in cells]
                    regions.append((rmin,cmin,h,w,vals))
    groups={}
    for rmin,cmin,h,w,vals in regions:
        groups.setdefault((h,w), []).append((rmin,cmin,vals))
    out=[[0]*C for _ in range(R)]
    for (h,w), regs in groups.items():
        if h==1:
            for rmin,cmin,vals in regs:
                cnt={}
                for v in vals:
                    cnt[v]=cnt.get(v,0)+1
                color=max(cnt.items(), key=lambda x:x[1])[0]
                for i in range(h):
                    for j in range(w):
                        out[rmin+i][cmin+j]=color
        else:
            P=[[None]*w for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    cnt={}
                    for rmin,cmin,vals in regs:
                        v=grid[rmin+i][cmin+j]
                        cnt[v]=cnt.get(v,0)+1
                    P[i][j]=max(cnt.items(), key=lambda x:x[1])[0]
            for rmin,cmin,vals in regs:
                for i in range(h):
                    for j in range(w):
                        out[rmin+i][cmin+j]=P[i][j]
    return out