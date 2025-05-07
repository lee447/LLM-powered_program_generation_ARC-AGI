from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    pattern = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                stack = [(i,j)]
                comp = []
                colors = set()
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    colors.add(grid[x][y])
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]!=0:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                if len(colors)>1:
                    pattern = comp
                    break
        if pattern:
            break
    r0 = min(r for r,c in pattern)
    r1 = max(r for r,c in pattern)
    c0 = min(c for r,c in pattern)
    c1 = max(c for r,c in pattern)
    H = r1-r0+1
    W = c1-c0+1
    P = [grid[r0+i][c0:c0+W] for i in range(H)]
    out = [row[:] for row in grid]
    for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        if dx==1 and dy==1: continue
        rs = r0 if dx==1 else r1+1
        cs = c0 if dy==1 else c1+1
        mapping = {}
        for i in range(H):
            for j in range(W):
                ii, jj = rs+i, cs+j
                if 0<=ii<h and 0<=jj<w and grid[ii][jj]!=0:
                    pi = i if dx==1 else H-1-i
                    pj = j if dy==1 else W-1-j
                    mapping[P[pi][pj]] = grid[ii][jj]
        for i in range(H):
            for j in range(W):
                ii, jj = rs+i, cs+j
                if 0<=ii<h and 0<=jj<w and grid[ii][jj]==0:
                    pi = i if dx==1 else H-1-i
                    pj = j if dy==1 else W-1-j
                    out[ii][jj] = mapping.get(P[pi][pj],0)
    return out