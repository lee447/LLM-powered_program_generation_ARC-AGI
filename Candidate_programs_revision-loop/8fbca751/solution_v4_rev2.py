from collections import deque
def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    boxes=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not vis[i][j]:
                vis[i][j]=True
                dq=deque([(i,j)])
                minr=maxr=i;minc=maxc=j
                while dq:
                    r,c=dq.popleft()
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==8:
                            vis[nr][nc]=True
                            dq.append((nr,nc))
                            minr=min(minr,nr);maxr=max(maxr,nr)
                            minc=min(minc,nc);maxc=max(maxc,nc)
                boxes.append([minr,maxr,minc,maxc])
    changed=True
    while changed:
        changed=False
        n=len(boxes)
        for i in range(n):
            for j in range(i+1,n):
                a=boxes[i];b=boxes[j]
                if (a[1]+1==b[0] or b[1]+1==a[0]) and max(a[2],b[2])<=min(a[3],b[3]):
                    boxes[i]=[min(a[0],b[0]),max(a[1],b[1]),min(a[2],b[2]),max(a[3],b[3])]
                    boxes.pop(j);changed=True;break
                if (a[3]+1==b[2] or b[3]+1==a[2]) and max(a[0],b[0])<=min(a[1],b[1]):
                    boxes[i]=[min(a[0],b[0]),max(a[1],b[1]),min(a[2],b[2]),max(a[3],b[3])]
                    boxes.pop(j);changed=True;break
            if changed:break
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in boxes:
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):
                if out[r][c]==0:out[r][c]=2
    return out