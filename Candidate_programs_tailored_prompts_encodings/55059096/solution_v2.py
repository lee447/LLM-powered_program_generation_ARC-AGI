def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    n=len(centers)
    for i in range(n):
        r1,c1=centers[i]
        for j in range(i+1,n):
            r2,c2=centers[j]
            dr=r2-r1;dc=c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1
                sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i,(r1,c1) in enumerate(centers):
        for r2,c2 in centers[i+1:]:
            dr=r2-r1;dc=c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1
                sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i in range(len(centers)):
        r1,c1=centers[i]
        for j in range(i+1,len(centers)):
            r2,c2=centers[j]
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1; sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h,len_grid= len(grid), len(grid)
    w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i in range(len(centers)):
        r1,c1=centers[i]
        for r2,c2 in centers[i+1:]:
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1
                sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i,(r1,c1) in enumerate(centers):
        for r2,c2 in centers[i+1:]:
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1; sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i in range(len(centers)):
        r1,c1=centers[i]
        for j in range(i+1,len(centers)):
            r2,c2=centers[j]
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1; sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i in range(len(centers)):
        r1,c1=centers[i]
        for j in range(i+1,len(centers)):
            r2,c2=centers[j]
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1
                sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    for i in range(len(centers)):
        r1,c1=centers[i]
        for j in range(i+1,len(centers)):
            r2,c2=centers[j]
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1; sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res
def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    cs=[]
    for i in range(1,h-1):
        for j in range(1,w-1):
            if grid[i][j]==3 and grid[i-1][j]==3 and grid[i+1][j]==3 and grid[i][j-1]==3 and grid[i][j+1]==3:
                cs.append((i,j))
    for a in range(len(cs)):
        r1,c1=cs[a]
        for r2,c2 in cs[a+1:]:
            dr,dc=r2-r1,c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                sr=1 if dr>0 else -1; sc=1 if dc>0 else -1
                for k in range(1,abs(dr)):
                    res[r1+k*sr][c1+k*sc]=2
    return res