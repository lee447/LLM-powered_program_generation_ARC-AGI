from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==3:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                comps.append((min(rs),max(rs),min(cs),max(cs),comp))
    boxes = sorted(comps, key=lambda b: (b[0],b[2]))
    new = [[0]*w for _ in range(h)]
    for minr,maxr,minc,maxc,comp in boxes:
        for x,y in comp:
            new[x][y] = 3
    for a,b in zip(boxes, boxes[1:]):
        a_minr,a_maxr,a_minc,a_maxc,_ = a
        b_minr,b_maxr,b_minc,b_maxc,_ = b
        if a_minr<=b_maxr and b_minr<=a_maxr:
            y = max(a_minr,b_minr)+1
            for x in range(a_maxc+1, b_minc):
                new[y][x] = 3
        else:
            x = max(a_minc,b_minc)+1
            for y in range(a_maxr+1, b_minr):
                new[y][x] = 3
    return new