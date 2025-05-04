def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    from collections import deque
    colors = set(c for row in grid for c in row if c!=0)
    comps = {}
    for c in colors:
        seen = [[False]*W for _ in range(H)]
        lst = []
        for i in range(H):
            for j in range(W):
                if grid[i][j]==c and not seen[i][j]:
                    q = deque([(i,j)])
                    seen[i][j]=True
                    cells = []
                    while q:
                        x,y = q.popleft()
                        cells.append((x,y))
                        for dx,dy in dirs:
                            nx,ny = x+dx,y+dy
                            if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==c:
                                seen[nx][ny]=True
                                q.append((nx,ny))
                    lst.append(cells)
        comps[c] = lst
    # choose left/right by min_x of each color
    mins = {c: min(y for x,y in cells for cells in comps[c]) for c in colors}
    col_list = sorted(colors, key=lambda c: mins[c])
    left, right = col_list[0], col_list[1]
    # find left max width
    def bbox(cells):
        rs = [x for x,y in cells]; cs = [y for x,y in cells]
        return min(rs), min(cs), max(rs), max(cs)
    left_wmax = 0
    for comp in comps[left]:
        _, c0, _, c1 = bbox(comp)
        left_wmax = max(left_wmax, c1-c0+1)
    xoff = {left: 0, right: left_wmax+1}
    out = [[0]*W for _ in range(H)]
    for c in [left, right]:
        lst = comps[c]
        # sort by size ascending
        lst.sort(key=lambda comp: len(comp))
        small, big = lst[0], lst[1]
        r0s, c0s, r1s, c1s = bbox(small)
        h0, w0 = r1s-r0s+1, c1s-c0s+1
        r0b, c0b, r1b, c1b = bbox(big)
        h1, w1 = r1b-r0b+1, c1b-c0b+1
        yb = H - h1
        ys = yb - h0 - 1
        xo = xoff[c]
        for x,y in small:
            out[ys + (x-r0s)][xo + (y-c0s)] = c
        for x,y in big:
            out[yb + (x-r0b)][xo + (y-c0b)] = c
    return out