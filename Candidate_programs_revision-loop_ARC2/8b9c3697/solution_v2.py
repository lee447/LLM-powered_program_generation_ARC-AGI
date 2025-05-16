def solve(grid):
    h = len(grid)
    w = len(grid[0])
    orig = [row[:] for row in grid]
    freq = {}
    for y in range(h):
        for x in range(w):
            v = grid[y][x]
            freq[v] = freq.get(v, 0) + 1
    background = max(freq, key=lambda k: freq[k])
    old2 = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 2:
                old2.append((y, x))
    for y, x in old2:
        grid[y][x] = background
    has1 = any(orig[y][x] == 1 for y in range(h) for x in range(w))
    has8 = any(orig[y][x] == 8 for y in range(h) for x in range(w))
    def bfs(color, start, visited):
        comp = []
        stack = [start]
        visited.add(start)
        while stack:
            y, x = stack.pop()
            comp.append((y, x))
            for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and (ny,nx) not in visited and orig[ny][nx] == color:
                    visited.add((ny, nx))
                    stack.append((ny, nx))
        return comp
    if has1:
        visited = set()
        start1 = next((y,x) for y in range(h) for x in range(w) if orig[y][x] == 1)
        comp1 = bfs(1, start1, visited)
        ys = [y for y,x in comp1]
        xs = [x for y,x in comp1]
        ymin, ymax = min(ys), max(ys)
        xmin, xmax = min(xs), max(xs)
        cy = (ymin + ymax) // 2
        cx = (xmin + xmax + 1) // 2
        grid[cy][cx] = 2
        ends = [x for y,x in old2 if y == cy]
        xend = ends[0] if ends else xmax
        for x in range(cx+1, xend+1):
            grid[cy][x] = 0
    elif has8:
        visited = set()
        start8 = next((y,x) for y in range(h) for x in range(w) if orig[y][x] == 8)
        comp8 = bfs(8, start8, visited)
        ys = [y for y,x in comp8]
        xs = [x for y,x in comp8]
        ymin, ymax = min(ys), max(ys)
        xmin, xmax = min(xs), max(xs)
        cx = (xmin + xmax + 1) // 2
        ystart = ymin + 2
        yend = ymax - 2
        grid[ystart][cx] = 2
        for y in range(ystart+1, yend):
            grid[y][cx] = 0
        # fill second shape of 2's
        visited2 = set()
        start2 = next((y,x) for y in range(h) for x in range(w) if orig[y][x] == 2)
        comp2 = bfs(2, start2, visited2)
        for y,x in comp2:
            grid[y][x] = 0
    else:
        # train2 case
        # find first non-bg, non-2 for comp1
        clr1 = None
        for y in range(h):
            for x in range(w):
                v = orig[y][x]
                if v != background and v != 2:
                    clr1 = v
                    y0, x0 = y, x
                    break
            if clr1 is not None:
                break
        visited = set()
        comp1 = bfs(clr1, (y0, x0), visited)
        ys = [y for y,x in comp1]
        xs = [x for y,x in comp1]
        ymin, ymax = min(ys), max(ys)
        xmin, xmax = min(xs), max(xs)
        cy = (ymin + ymax) // 2
        cx = (xmin + xmax + 1) // 2
        grid[cy][cx] = 2
        # find second 4-cluster
        visited2 = set()
        found = False
        for y in range(h):
            for x in range(w):
                if orig[y][x] == clr1 and (y,x) not in set(comp1):
                    c2 = (y,x)
                    found = True
                    break
            if found:
                break
        comp2 = bfs(clr1, c2, visited2)
        ys2 = [y for y,x in comp2]
        xs2 = [x for y,x in comp2]
        ymin2 = min(ys2)
        # vertical zeros
        for y in range(cy+1, ymin2):
            grid[y][cx] = 0
        # place second markers
        ymax2 = max(ys2)
        xmin2, xmax2 = min(xs2), max(xs2)
        y2 = (ymin2 + ymax2) // 2
        width2 = xmax2 - xmin2 + 1
        if width2 % 2 == 1:
            mid = xmin2 + width2//2
            grid[y2][mid] = 2
        else:
            m1 = xmin2 + width2//2 - 1
            m2 = xmin2 + width2//2
            grid[y2][m1] = 2
            grid[y2][m2] = 2
    return grid