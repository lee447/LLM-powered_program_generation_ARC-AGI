import itertools
def solve(grid):
    from collections import Counter
    n,m=len(grid),len(grid[0])
    # find the marker color and its bounding box
    marker=None
    for c in set(itertools.chain.from_iterable(grid)):
        pts=[(i,j) for i in range(n) for j in range(m) if grid[i][j]==c]
        if len(pts)>1:
            rs=[i for i,_ in pts]; cs=[j for _,j in pts]
            h=max(rs)-min(rs)+1; w=max(cs)-min(cs)+1
            if h*w==len(pts):
                if marker is None or len(pts)>sum(x==marker for row in grid for x in row):
                    marker=c; br,bc,hr,hc=min(rs),min(cs),h,w
    # build skip‐mask prefix sums
    skip=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            skip[i+1][j+1]=skip[i][j+1]+skip[i+1][j]-skip[i][j]+(grid[i][j]==marker)
    def has_marker(i,j,h,w):
        i2,j2=i+h,j+w
        return skip[i2][j2]-skip[i][j2]-skip[i2][j]+skip[i][j]>0
    best_score=-1
    best_block=None
    for h in range(1,n+1):
        for w in range(1,m+1):
            if h*w<=1: continue
            cnt=Counter()
            for i in range(n-h+1):
                for j in range(m-w+1):
                    if not has_marker(i,j,h,w):
                        blk=tuple(tuple(grid[i+di][j+dj] for dj in range(w)) for di in range(h))
                        cnt[blk]+=1
            if cnt:
                blk,ct=cnt.most_common(1)[0]
                score=ct*h*w
                if score>best_score:
                    best_score=score
                    best_block=blk
    return [list(r) for r in best_block]