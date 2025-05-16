from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    bg=max({c:sum(row.count(c) for row in grid) for row in grid}, key=lambda k:{c:sum(row.count(c) for row in grid) for k,c in enumerate(grid)}.get)
    mask=[[grid[r][c]!=bg for c in range(w)] for r in range(h)]
    rowsum=[any(mask[r][c] for c in range(w)) for r in range(h)]
    colsum=[any(mask[r][c] for r in range(h)) for c in range(w)]
    def find_gap(arr,n):
        best=(0,0,0)
        i=0
        while i<n:
            if not arr[i]:
                j=i
                while j<n and not arr[j]: j+=1
                if i>0 and j<n and j-i>best[2]:
                    best=(i,j,j-i)
                i=j
            else:
                i+=1
        return best[0],best[1]
    r0,r1=find_gap(rowsum,h)
    c0,c1=find_gap(colsum,w)
    vis=[[False]*w for _ in range(h)]
    quads={}
    for i in range(h):
        for j in range(w):
            if mask[i][j] and not vis[i][j]:
                col=grid[i][j]
                q=deque([(i,j)]);vis[i][j]=True;pts_abs=[]
                while q:
                    r,c=q.popleft();pts_abs.append((r,c))
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=c+dc, r+dr
                        if 0<=rr<h and 0<=cc<w and mask[rr][cc] and not vis[rr][cc]:
                            vis[rr][cc]=True;q.append((rr,cc))
                rs=[p[0] for p in pts_abs];cs=[p[1] for p in pts_abs]
                minr,minc=min(rs),min(cs)
                pts=[(r-minr,c-minc) for r,c in pts_abs]
                cen_r=sum(rs)/len(rs);cen_c=sum(cs)/len(cs)
                top=cen_r<r0
                left=cen_c<c0
                key=('T' if top else 'B')+('L' if left else 'R')
                quads[key]=(col,pts,min(rs),min(cs))
    def dim(sh):return max(r for r,c in sh[1])+1,max(c for r,c in sh[1])+1
    hTL,wTL=dim(quads['TL']);hTR,wTR=dim(quads['TR'])
    hBL,wBL=dim(quads['BL']);hBR,wBR=dim(quads['BR'])
    top_h=max(hTL,hTR);bot_h=max(hBL,hBR)
    left_w=max(wTL,wBL);right_w=max(wTR,wBR)
    H=top_h+1+bot_h;W=left_w+1+right_w
    out=[[bg]*W for _ in range(H)]
    def place(sh,orow,ocol):
        col,pts,_,_=sh
        for dr,dc in pts: out[orow+dr][ocol+dc]=col
    place(quads['TL'],0,0)
    place(quads['TR'],0,left_w+1)
    place(quads['BL'],top_h+1,0)
    place(quads['BR'],top_h+1,left_w+1)
    return out