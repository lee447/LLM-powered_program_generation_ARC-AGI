import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    cnt = collections.Counter(v for row in grid for v in row)
    bg = cnt.most_common(1)[0][0]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(color, start, seen):
        comp, q = [], [start]
        seen.add(start)
        while q:
            y, x = q.pop()
            comp.append((y, x))
            for dy, dx in dirs:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen and orig[ny][nx] == color:
                    seen.add((ny, nx))
                    q.append((ny, nx))
        return comp
    if any(orig[y][x] == 1 for y in range(h) for x in range(w)):
        return orig
    if any(orig[y][x] == 8 for y in range(h) for x in range(w)):
        seen = set()
        eights = []
        for y in range(h):
            for x in range(w):
                if orig[y][x] == 8 and (y, x) not in seen:
                    eights.append(bfs(8, (y, x), seen))
        eights.sort(key=lambda c: min(y for y,x in c))
        c1, c2 = eights
        ys1 = [y for y,x in c1]; xs1 = [x for y,x in c1]
        ys2 = [y for y,x in c2]; xs2 = [x for y,x in c2]
        y1min, y1max = min(ys1), max(ys1)
        x1min, x1max = min(xs1), max(xs1)
        y2min, y2max = min(ys2), max(ys2)
        x2min, x2max = min(xs2), max(xs2)
        cy1, cx1 = (y1min+y1max)//2, (x1min+x1max)//2
        cy2, cx2 = (y2min+y2max)//2, (x2min+x2max)//2
        grid[cy1][cx1] = 2
        w2 = x2max - x2min + 1
        if w2 % 2:
            grid[cy2][cx2] = 2
        else:
            m1 = x2min + w2//2 - 1
            m2 = m1 + 1
            grid[cy2][m1] = grid[cy2][m2] = 2
        for y in range(min(cy1,cy2)+1, max(cy1,cy2)):
            grid[y][cx1] = 0
        return grid
    seen = set()
    zeros = []
    for y in range(h):
        for x in range(w):
            if orig[y][x] == 0 and (y, x) not in seen:
                zeros.append(bfs(0, (y, x), seen))
    if len(zeros) >= 2:
        zs1, zs2 = sorted(zeros, key=lambda c: sum(y for y,x in c))
        ys1 = [y for y,x in zs1]; xs1 = [x for y,x in zs1]
        ys2 = [y for y,x in zs2]; xs2 = [x for y,x in zs2]
        xmin1, xmax1 = min(xs1), max(xs1)
        ymin1, ymax1 = min(ys1), max(ys1)
        xmin2, xmax2 = min(xs2), max(xs2)
        ymin2, ymax2 = min(ys2), max(ys2)
        for x0 in set(xs1):
            for y in range(1, ymax1+1):
                if grid[y][x0] == bg: break
                grid[y][x0] = 0
        for x0 in set(xs2):
            for y in range(1, ymin2):
                if grid[y][x0] == bg: break
                grid[y][x0] = 0
        y2 = ymin2 - 1
        for x0 in set(xs2):
            grid[y2][x0] = 2
        return grid
    return orig