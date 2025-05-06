def solve(grid):
    h=len(grid); w=len(grid[0])
    orig=[row[:] for row in grid]
    res=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    dirs=[(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) if dx or dy]
    for i in range(h):
        for j in range(w):
            if orig[i][j]==8 and not visited[i][j]:
                stack=[(i,j)]
                visited[i][j]=True
                comp=[]
                while stack:
                    x,y=stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and orig[nx][ny]==8:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                minr=min(x for x,_ in comp); maxr=max(x for x,_ in comp)
                minc=min(y for _,y in comp); maxc=max(y for _,y in comp)
                for c in range(minc,maxc+1):
                    if orig[minr][c]!=8: res[minr][c]=2
                    if orig[maxr][c]!=8: res[maxr][c]=2
                for r in range(minr,maxr+1):
                    if orig[r][minc]!=8: res[r][minc]=2
                    if orig[r][maxc]!=8: res[r][maxc]=2
    return res