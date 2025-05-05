from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    nodes = []
    start = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and not seen[r][c]:
                col = grid[r][c]
                q = deque([(r,c)])
                comp = []
                seen[r][c] = True
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                if col == 2 and len(comp)==1:
                    start = comp[0]
                elif len(comp) == 3:
                    xs = [x for x,y in comp]
                    ys = [y for x,y in comp]
                    if xs[0]==xs[1]==xs[2]:
                        r0 = xs[0]
                        c0 = sum(ys)//3
                        nodes.append((r0,c0))
                    else:
                        c0 = ys[0]
                        r0 = sum(xs)//3
                        nodes.append((r0,c0))
    nodes.sort()
    if start:
        nodes = [start] + nodes
    out = [row[:] for row in grid]
    for (r1,c1),(r2,c2) in zip(nodes, nodes[1:]):
        if r1 == r2:
            for y in range(min(c1,c2)+1, max(c1,c2)):
                if out[r1][y] == 0:
                    out[r1][y] = 2
        elif c1 == c2:
            for x in range(min(r1,r2)+1, max(r1,r2)):
                if out[x][c1] == 0:
                    out[x][c1] = 2
        else:
            for x in range(min(r1,r2)+1, max(r1,r2)):
                if out[x][c1] == 0:
                    out[x][c1] = 2
            for y in range(min(c1,c2)+1, max(c1,c2)):
                if out[r2][y] == 0:
                    out[r2][y] = 2
    return out