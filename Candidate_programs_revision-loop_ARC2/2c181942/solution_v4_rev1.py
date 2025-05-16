from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0]);bg=8
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
                    best=(i,j-1,j-i)
                i=j
            else: i+=1
        return best[0],best[1]
    r0,r1=find_gap(rowsum,h)
    c0,c1=find_gap(colsum,w)
    vis=[[False]*w for _ in range(h)]
    shapes={}
    for i in range(h):
        for j in range(w):
            if mask[i][j] and not vis[i][j]:
                col=grid[i][j]
                q=deque([(i,j)]);vis[i][j]=True;cc=[]
                while q:
                    r,c=q.popleft();cc.append((r,c))
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc2=r+dr,c+dc
                        if 0<=rr<h and 0<=cc2<w and mask[rr][cc2] and not vis[rr][cc2]:
                            vis[rr][cc2]=True;q.append((rr,cc2))
                rs=[p[0] for p in cc];cs=[p[1] for p in cc]
                mr,Mc=min(rs),min(cs)
                pts=[(r-mr,c-Mc) for r,c in cc]
                cen_r=sum(rs)/len(rs);cen_c=sum(cs)/len(cs)
                if cen_r<r0 and cen_c<c0:key='TL'
                elif cen_r<r0 and cen_c>c1:key='TR'
                elif cen_r>r1 and cen_c<c0:key='BL'
                else:key='BR'
                shapes[key]=(col,pts)
    def dim(sh):
        _,pts=sh
        rs=[p[0] for p in pts];cs=[p[1] for p in pts]
        return max(rs)+1,max(cs)+1
    hTL,wTL=dim(shapes['TL']);hTR,wTR=dim(shapes['TR'])
    hBL,wBL=dim(shapes['BL']);hBR,wBR=dim(shapes['BR'])
    top_h=max(hTL,hTR);bot_h=max(hBL,hBR);left_w=max(wTL,wBL);right_w=max(wTR,wBR)
    H=top_h+1+bot_h;W=left_w+1+right_w
    out=[[bg]*W for _ in range(H)]
    def place(sh,orow,ocol):
        col,pts=sh
        for dr,dc in pts: out[orow+dr][ocol+dc]=col
    place(shapes['TL'],0,0)
    place(shapes['TR'],0,left_w+1)
    place(shapes['BL'],top_h+1,0)
    place(shapes['BR'],top_h+1,left_w+1)
    return out