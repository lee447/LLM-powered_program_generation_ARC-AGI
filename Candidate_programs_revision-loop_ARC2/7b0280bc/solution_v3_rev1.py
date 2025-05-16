from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    counts={}
    for i in range(h):
        for j in range(w):
            counts[grid[i][j]]=counts.get(grid[i][j],0)+1
    bg=max(counts,key=lambda c:counts[c])
    colors=[c for c in counts if c!=bg]
    perim=set()
    for x in range(w):
        perim.add((0,x));perim.add((h-1,x))
    for y in range(h):
        perim.add((y,0));perim.add((y,w-1))
    rec=[c for c in colors if any(grid[i][j]==c for i,j in perim)]
    if len(rec)==2:
        a,b=sorted(rec)
        out=[row[:]for row in grid]
        for i in range(h):
            for j in range(w):
                if grid[i][j]==a: out[i][j]=5
                elif grid[i][j]==b: out[i][j]=3
        return out
    asc=sorted(colors,key=lambda c:counts[c])
    c_small, c_mid = asc[0], asc[1]
    c_largest = max(colors, key=lambda c:(counts[c],c))
    def bfs_color(c):
        vis=[[False]*w for _ in range(h)]
        dq=deque()
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni,nj=i+di,j+dj
                        if 0<=ni<h and 0<=nj<w and grid[ni][nj]==bg and not vis[ni][nj]:
                            vis[ni][nj]=True
                            dq.append((ni,nj))
        while dq:
            i,j=dq.popleft()
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<h and 0<=nj<w and grid[ni][nj]==bg and not vis[ni][nj]:
                    vis[ni][nj]=True
                    dq.append((ni,nj))
        return vis
    vis_L=bfs_color(c_largest)
    out=[row[:]for row in grid]
    vs=bfs_color(c_small)
    for i in range(h):
        for j in range(w):
            if grid[i][j]==bg and vs[i][j] and vis_L[i][j]:
                out[i][j]=3
    vm=bfs_color(c_mid)
    for i in range(h):
        for j in range(w):
            if grid[i][j]==bg and vm[i][j] and vis_L[i][j]:
                out[i][j]=5
    return out