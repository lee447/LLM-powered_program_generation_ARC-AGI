def solve(grid):
    h = len(grid)
    w = len(grid[0])
    first_zero = next(i for i,row in enumerate(grid) if any(v==0 for v in row))
    last_zero = h-1 - next(i for i,row in enumerate(reversed(grid)) if any(v==0 for v in row))
    top = grid[:first_zero]
    bottom = grid[last_zero+1:]
    anchors = []
    for r in range(first_zero):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5:
                anchors.append((r,c))
    out = [list(row) for row in top]
    for r in range(last_zero+1,h):
        out.append(list(grid[r]))
    for r,c in anchors:
        mirror = first_zero + (h-1-last_zero) - (r-first_zero) - 1
        if 0<=mirror<len(out):
            for dr in (0,1):
                for dc in (0,1):
                    out[mirror+dr][c+dc] = 5
    frame = [[grid[0][0]]*w]
    frame += out
    while len(frame)<h:
        frame.append(frame[-1][:])
    return frame