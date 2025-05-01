def solve(grid):
    h = len(grid)
    w = len(grid[0])
    new = [row[:] for row in grid]
    segs = []
    for r in range(h):
        c = 0
        while c < w:
            if grid[r][c] != 0:
                v = grid[r][c]
                start = c
                while c + 1 < w and grid[r][c + 1] == v:
                    c += 1
                end = c
                if end > start:
                    segs.append((r, start, end, v))
                c += 1
            else:
                c += 1
    segs.sort(key=lambda x: x[0])
    n = len(segs)
    internals = segs[1:n-1]
    cnt = len(internals)
    for i, (r, start, end, v) in enumerate(internals):
        sh = 1 if cnt == 1 else i
        for c in range(start, end+1):
            new[r][c] = 0
        for c in range(start, end+1):
            new[r][c+sh] = v
    return new