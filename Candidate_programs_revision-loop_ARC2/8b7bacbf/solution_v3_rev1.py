import sys
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    vis = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                comp = []
                while stack:
                    x, y = stack.pop()
                    comp.append((x,y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != 0 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                colors = {grid[x][y] for x,y in comp}
                if len(colors) == 2:
                    for interior_color in colors:
                        ok_int = True
                        for x,y in comp:
                            if grid[x][y] == interior_color:
                                for dx,dy in dirs:
                                    nx, ny = x+dx, y+dy
                                    if not (0 <= nx < H and 0 <= ny < W) or grid[nx][ny] == 0:
                                        ok_int = False
                                        break
                                if not ok_int:
                                    break
                        if not ok_int:
                            continue
                        border_color = (colors - {interior_color}).pop()
                        ok_border = True
                        for x,y in comp:
                            if grid[x][y] == border_color:
                                has_bg = False
                                for dx,dy in dirs:
                                    nx, ny = x+dx, y+dy
                                    if not (0 <= nx < H and 0 <= ny < W) or grid[nx][ny] == 0:
                                        has_bg = True
                                        break
                                if not has_bg:
                                    ok_border = False
                                    break
                        if not ok_border:
                            continue
                        for x,y in comp:
                            if grid[x][y] == interior_color:
                                out[x][y] = 0
                        break
    return out