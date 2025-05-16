from collections import deque
def solve(grid):
    n, m = len(grid), len(grid[0])
    bg = max(range(10), key=lambda c: sum(row.count(c) for row in grid))
    threes = [(i,j) for i in range(n) for j in range(m) if grid[i][j]==3]
    r0 = max(i for i,j in threes)
    c0 = max(j for i,j in threes)
    def quad(i,j):
        if i<r0 and j<c0: return 1
        if i<r0 and j>c0: return 2
        if i>r0 and j<c0: return 3
        if i>r0 and j>c0: return 4
        return 0
    cnt = {q:0 for q in (1,2,3,4)}
    for i in range(n):
        for j in range(m):
            q=quad(i,j)
            if q and grid[i][j]!=bg and grid[i][j]!=3:
                cnt[q]+=1
    target = max(cnt, key=lambda q: cnt[q])
    seen=[[False]*m for _ in range(n)]
    best_comp=[]
    for i in range(n):
        for j in range(m):
            if not seen[i][j] and quad(i,j)==target and grid[i][j]!=bg and grid[i][j]!=3:
                comp=[]
                dq=deque([(i,j)])
                seen[i][j]=True
                while dq:
                    x,y=dq.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<m and not seen[nx][ny] and quad(nx,ny)==target and grid[nx][ny]!=bg and grid[nx][ny]!=3:
                            seen[nx][ny]=True
                            dq.append((nx,ny))
                if len(comp)>len(best_comp):
                    best_comp=comp
    out=[row[:] for row in grid]
    for i,j in best_comp:
        out[i][j]=bg
    return out