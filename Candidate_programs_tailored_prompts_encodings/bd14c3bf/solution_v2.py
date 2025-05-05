def solve(grid):
    h=len(grid); w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not visited[i][j]:
                val=grid[i][j]
                stack=[(i,j)]; cells=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and grid[rr][cc]!=0 and not visited[rr][cc]:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                comps.append({'cells':cells,'val':val})
    n=len(comps)
    def mirror_pair(a,b):
        if len(a['cells'])!=len(b['cells']): return False
        ra={}
        rb={}
        for r,c in a['cells']: ra.setdefault(r,[]).append(c)
        for r,c in b['cells']: rb.setdefault(r,[]).append(c)
        if set(ra.keys())!=set(rb.keys()): return False
        X=None
        for r in ra:
            ca=sorted(ra[r]); cb=sorted(rb[r])
            if len(ca)!=len(cb): return False
            m=len(ca)
            for k in range(m):
                x=(ca[k]+cb[m-1-k])/2
                if X is None: X=x
                elif abs(X-x)>1e-6: return False
        return True
    pair={}
    for i in range(n):
        for j in range(i+1,n):
            if mirror_pair(comps[i],comps[j]):
                pair[i]=j; pair[j]=i
    newval=[0]*n
    for i in range(n):
        if i in pair:
            j=pair[i]
            if i<j:
                avg_i=sum(c for r,c in comps[i]['cells'])/len(comps[i]['cells'])
                avg_j=sum(c for r,c in comps[j]['cells'])/len(comps[j]['cells'])
                left, right = (i,j) if avg_i<avg_j else (j,i)
                v=comps[left]['val']
                newval[left]=v; newval[right]=v
        else:
            newval[i]=2
    out=[[0]*w for _ in range(h)]
    for i,comp in enumerate(comps):
        for r,c in comp['cells']:
            out[r][c]=newval[i]
    return out