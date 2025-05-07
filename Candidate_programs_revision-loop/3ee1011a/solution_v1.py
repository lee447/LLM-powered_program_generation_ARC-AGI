def solve(grid):
    h=len(grid);w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    clusters=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not visited[i][j]:
                col=grid[i][j]
                stack=[(i,j)]
                visited[i][j]=True
                cells=[]
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                clusters.append((len(cells),col))
    clusters.sort(reverse=True)
    sizes=[sz for sz,_ in clusters]
    colors=[c for _,c in clusters]
    N=sizes[0]
    res=[[0]*N for _ in range(N)]
    k=len(clusters)
    for i in range(k-1):
        c=colors[i]
        o=i;l=N-1-i
        for x in range(o,l+1):
            res[o][x]=c;res[l][x]=c
        for y in range(o+1,l):
            res[y][o]=c;res[y][l]=c
    last=colors[k-1]
    o=k-1;L=sizes[k-1]
    for i in range(o,o+L):
        for j in range(o,o+L):
            res[i][j]=last
    return res