import itertools
def solve(grid):
    h,w=len(grid),len(grid[0])
    mask=grid[h-2]
    base=grid[h-1]
    drops=[i for i,x in enumerate(mask) if x==0]
    segs=[]
    for c in drops:
        if not segs or c!=segs[-1][-1]+1:
            segs.append([c])
        else:
            segs[-1].append(c)
    visited=[[False]*w for _ in range(h)]
    shapes=[]
    for r in range(h-2):
        for c in range(w):
            if grid[r][c]!=0 and not visited[r][c]:
                col=grid[r][c]
                stack=[(r,c)]
                visited[r][c]=True
                cells=[]
                while stack:
                    y,x=stack.pop()
                    cells.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx=y+dy, x+dx
                        if 0<=ny<h-2 and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                xs=[x for y,x in cells]
                ys=[y for y,x in cells]
                minc,minr=min(xs),min(ys)
                maxc=max(xs)
                cnt=len(cells)
                width=maxc-minc+1
                shapes.append((minc,minr,col,cnt,width))
    shapes.sort(key=lambda x:(x[0],x[1]))
    n=len(shapes)
    m=len(segs)
    best=None
    best_perm=None
    for perm in itertools.permutations(range(m),n):
        used=set()
        valid=True
        pen=0
        shift=0
        for i,si in enumerate(shapes):
            j=perm[i]
            if j in used or si[3]%len(segs[j])!=0:
                valid=False;break
            used.add(j)
            if si[4]!=len(segs[j]):
                pen+=1
            shift+=abs(si[0]-segs[j][0])
        if not valid: continue
        key=(pen,shift)
        if best is None or key<best:
            best=key
            best_perm=perm
    out=[[0]*w for _ in range(h)]
    out[h-1]=base[:]
    out[h-2]=mask[:]
    for i,si in enumerate(shapes):
        seg=segs[best_perm[i]]
        L=len(seg)
        H=si[3]//L
        for dy in range(H):
            for c in seg:
                out[h-2-dy][c]=si[2]
    return out