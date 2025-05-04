import collections
def solve(grid):
    from collections import deque
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    bg = collections.Counter([grid[0][x] for x in range(W)] +
                             [grid[H-1][x] for x in range(W)] +
                             [grid[y][0] for y in range(1,H-1)] +
                             [grid[y][W-1] for y in range(1,H-1)]).most_common(1)[0][0]
    seen = [[False]*W for _ in range(H)]
    shapes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != bg and not seen[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                cells = []
                while q:
                    y,x = q.popleft()
                    cells.append((y,x))
                    for dy,dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and not seen[ny][nx] and grid[ny][nx]==c:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                rs = [r for r,_ in cells]; cs = [c0 for _,c0 in cells]
                minr, maxr = min(rs), max(rs)
                minc, maxc = min(cs), max(cs)
                sub = [row[minc:maxc+1] for row in grid[minr:maxr+1]]
                shapes.append((len(cells), c, sub))
    shapes.sort(reverse=True, key=lambda x: x[0])
    if not shapes:
        return grid
    _, main_col, main_sub = shapes[0]
    H2, W2 = len(main_sub), len(main_sub[0])
    canvas = [[main_col]*W2 for _ in range(H2)]
    for _, col, sub in shapes[1:]:
        h, w = len(sub), len(sub[0])
        for i in range(h):
            for j in range(w):
                if sub[i][j]==col and (i==0 or i==h-1 or j==0 or j==w-1):
                    if 0<=i<H2 and 0<=j<W2:
                        canvas[i][j] = col
    return canvas