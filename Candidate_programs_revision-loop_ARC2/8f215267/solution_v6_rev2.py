from collections import deque, Counter

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = Counter(c for row in grid for c in row).most_common(1)[0][0]
    out = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c == bg or seen[y][x]:
                continue
            q = deque([(x,y)])
            comp = []
            seen[y][x] = True
            while q:
                cx, cy = q.popleft()
                comp.append((cx, cy))
                for dx, dy in dirs:
                    nx, ny = cx+dx, cy+dy
                    if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and grid[ny][nx] == c:
                        seen[ny][nx] = True
                        q.append((nx, ny))
            xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
            x0, x1 = min(xs), max(xs)
            y0, y1 = min(ys), max(ys)
            per = 2*((x1-x0+1)+(y1-y0+1)-2)
            if len(comp) != per:
                continue
            iw, ih = x1-x0-1, y1-y0-1
            if iw <= 0 or ih <= 0:
                continue
            if x1-x0 > y1-y0 or x1-x0 == y1-y0:
                my = (y0+y1)//2
                for xx in range(x0+1, x1):
                    if out[my][xx] == bg and (xx+my)%2 == 0:
                        out[my][xx] = c
            if x1-x0 < y1-y0 or x1-x0 == y1-y0:
                mx = (x0+x1)//2
                for yy in range(y0+1, y1):
                    if out[yy][mx] == bg and (yy+mx)%2 == 0:
                        out[yy][mx] = c
    return out