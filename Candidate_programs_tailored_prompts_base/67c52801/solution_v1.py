from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    shapes = []
    for i in range(R-2):
        for j in range(C):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R-2 and 0 <= ny < C and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                is_, js = zip(*cells)
                i0, i1 = min(is_), max(is_)
                j0, j1 = min(js), max(js)
                shapes.append((i0, i1, j0, j1, col))
    shapes.sort(key=lambda x: x[0])
    out = [[0]*C for _ in range(R)]
    for j in range(C):
        out[R-2][j] = grid[R-2][j]
        out[R-1][j] = grid[R-1][j]
    occ = [R-1 if out[R-2][j]==0 else R-2 for j in range(C)]
    for i0, i1, j0, j1, col in shapes:
        h = i1 - i0 + 1
        drop_row = min(occ[j] for j in range(j0, j1+1)) - 1
        top = drop_row - (h-1)
        for ii in range(top, drop_row+1):
            for jj in range(j0, j1+1):
                out[ii][jj] = col
        for jj in range(j0, j1+1):
            occ[jj] = top
    return out