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
            y,x = q.pop()
            comp.append((y,x))
            for dy,dx in dirs:
                ny,nx = y+dy, x+dx
                if 0<=ny<h and 0<=nx<w and (ny,nx) not in seen and orig[ny][nx]==color:
                    seen.add((ny,nx))
                    q.append((ny,nx))
        return comp
    if any(orig[y][x]==1 for y in range(h) for x in range(w)):
        return orig
    if any(orig[y][x]==8 for y in range(h) for x in range(w)):
        seen = set(); eights = []
        for y in range(h):
            for x in range(w):
                if orig[y][x]==8 and (y,x) not in seen:
                    eights.append(bfs(8,(y,x),seen))
        eights.sort(key=lambda c: min(y for y,x in c))
        def bbox(c):
            ys = [y for y,x in c]; xs = [x for y,x in c]
            return min(ys), max(ys), min(xs), max(xs)
        c1, c2 = eights
        y1min,y1max,x1min,x1max = bbox(c1)
        y2min,y2max,x2min,x2max = bbox(c2)
        cy1, cx1 = (y1min+y1max)//2, (x1min+x1max)//2
        cy2 = (y2min+y2max)//2
        w2 = x2max-x2min+1
        grid[cy1][cx1] = 2
        if w2%2:
            cx2 = (x2min+x2max)//2
            grid[cy2][cx2] = 2
        else:
            m1 = x2min + w2//2 - 1
            m2 = x2min + w2//2
            grid[cy2][m1] = grid[cy2][m2] = 2
        for y in range(min(cy1,cy2)+1, max(cy1,cy2)):
            grid[y][cx1] = 0
        return grid
    seen = set(); twos = []
    for y in range(h):
        for x in range(w):
            if grid[y][x]==2 and (y,x) not in seen:
                twos.append(bfs(2,(y,x),seen))
    twos.sort(key=lambda c: sum(y for y,x in c))
    cA, cB = twos
    ysA = [y for y,x in cA]; xsA = [x for y,x in cA]
    ysB = [y for y,x in cB]; xsB = [x for y,x in cB]
    cyA, cxA = sum(ysA)//len(ysA), sum(xsA)//len(xsA)
    cyB, cxB = sum(ysB)//len(ysB), sum(xsB)//len(xsB)
    dx = 1 if cxB>cxA else -1 if cxB<cxA else 0
    dy = 1 if cyB>cyA else -1 if cyB<cyA else 0
    # fill zeros behind B
    pts = sorted(xsB)
    for x0 in pts:
        y,x = cyB, x0
        while 0<=y<h and 0<=x<w and grid[y][x]!=bg:
            grid[y][x] = 0
            y += dy; x += dx
    return grid