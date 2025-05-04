from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 6 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx in (-1,0,1):
                        for dy in (-1,0,1):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] in (6,8):
                                visited[nx][ny] = True
                                stack.append((nx,ny))
                minx = min(x for x,_ in comp)
                maxx = max(x for x,_ in comp)
                miny = min(y for _,y in comp)
                maxy = max(y for _,y in comp)
                if len(comp) >= 3 and maxx-minx+1 <= 3 and maxy-miny+1 <= 3:
                    for x in range(minx, maxx+1):
                        for y in range(miny, maxy+1):
                            if grid[x][y] != 6:
                                grid[x][y] = 4
    return grid