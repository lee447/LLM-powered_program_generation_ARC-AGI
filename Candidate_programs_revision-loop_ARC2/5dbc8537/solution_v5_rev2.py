from collections import deque, Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    row_walls = [i for i in range(h) if all(grid[i][j] == grid[i][0] for j in range(w))]
    col_walls = [j for j in range(w) if all(grid[i][j] == grid[0][j] for i in range(h))]
    def find_shapes(r0, r1, c0, c1, bg, wall):
        seen = [[False]*w for _ in range(h)]
        shapes = []
        for i in range(r0, r1):
            for j in range(c0, c1):
                c = grid[i][j]
                if c != bg and c != wall and not seen[i][j]:
                    q = deque([(i,j)])
                    seen[i][j] = True
                    pts = []
                    mi, ma, mj, Mj = i, i, j, j
                    while q:
                        x,y = q.popleft()
                        pts.append((x,y))
                        mi = min(mi, x); ma = max(ma, x)
                        mj = min(mj, y); Mj = max(Mj, y)
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            x2, y2 = x+dx, y+dy
                            if r0 <= x2 < r1 and c0 <= y2 < c1 and not seen[x2][y2] and grid[x2][y2] == c:
                                seen[x2][y2] = True
                                q.append((x2,y2))
                    shapes.append((mi, mj, ma, Mj, pts, c))
        return shapes
    if len(col_walls) >= 2:
        col_walls.sort()
        L, R = col_walls[0], col_walls[1]
        r0, r1 = 0, h
        c0, c1 = R+1, w
        cnt = Counter(grid[i][j] for i in range(r0, r1) for j in range(c0, c1))
        bg = cnt.most_common(1)[0][0]
        wall = grid[0][L]
        shapes = find_shapes(r0, r1, c0, c1, bg, wall)
        shapes.sort(key=lambda x:(x[0], x[1]))
        out = [row[:R+1] for row in grid]
        for i in range(h):
            for j in range(L+1, R):
                out[i][j] = bg
        region_w = R - (L+1)
        y_off = 0
        for mi, mj, ma, Mj, pts, col in shapes:
            ph = ma - mi + 1
            pw = Mj - mj + 1
            cx = L+1 + (region_w - pw)//2 - mj
            cy = y_off - mi
            for x,y in pts:
                out[x+cy][y+cx] = col
            y_off += ph
        return out
    elif len(row_walls) >= 2:
        row_walls.sort()
        T, B = row_walls[0], row_walls[1]
        r0, r1 = T+1, B
        c0, c1 = 0, w
        cnt = Counter(grid[i][j] for i in range(r0, r1) for j in range(c0, c1))
        bg = cnt.most_common(1)[0][0]
        wall = grid[T][0]
        shapes = find_shapes(r0, r1, c0, c1, bg, wall)
        shapes.sort(key=lambda x:(x[1], x[0]))
        h2 = B - (T+1)
        out = [[bg]*w for _ in range(h2)]
        x_off = 0
        for mi, mj, ma, Mj, pts, col in shapes:
            ph = ma - mi + 1
            pw = Mj - mj + 1
            cy = (h2 - ph)//2 - mi
            for x,y in pts:
                out[x+cy][y+x_off] = col
            x_off += pw
        return out
    else:
        return grid