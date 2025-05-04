from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    rects = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 3 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and grid[nx][ny]==3:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                is_,js = zip(*cells)
                rects.append((min(is_),max(is_),min(js),max(js)))
    top = []
    bot = []
    for mi,Ma,mj,MaJ in rects:
        if (mi+Ma)/2 < R/2:
            top.append((mi,Ma,mj,MaJ))
        else:
            bot.append((mi,Ma,mj,MaJ))
    out = [row[:] for row in grid]
    for group in (top, bot):
        if len(group)==2:
            A,B = sorted(group, key=lambda t: t[2])
            r1 = A[0]+1
            r2 = A[1]-1
            cs, ce = A[3], B[2]
            for r in (r1,r2):
                for j in range(cs, ce+1):
                    out[r][j] = 3
    return out