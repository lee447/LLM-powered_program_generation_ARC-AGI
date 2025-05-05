def solve(grid):
    h = len(grid)
    w = len(grid[0])
    zeros = [r for r in range(h) if all(grid[r][c]==0 for c in range(w))]
    bands = []
    for i in range(len(zeros)-1):
        a, b = zeros[i], zeros[i+1]
        if b > a+1:
            bands.append((a+1, b-1))
    M = len(bands)
    if M == 0:
        return grid
    if M == 2:
        strokes = [(1, 'both')]
    elif M == 3:
        strokes = [(1, 'h'), (2, 'v')]
    else:
        strokes = [(M-2, 'h'), (M-1, 'v')]
    out = [row[:] for row in grid]
    for bi, orient in strokes:
        r0, r1 = bands[bi]
        top = r0
        # find block starts in this band by scanning top row
        runs = []
        c = 0
        while c < w:
            if grid[top][c] != 0:
                start = c
                while c < w and grid[top][c] != 0:
                    c += 1
                runs.append((start, c-1))
            else:
                c += 1
        if not runs:
            continue
        c0 = runs[0][0]
        color = grid[top][c0]
        if orient in ('h','both'):
            rr = top+2
            for dx in range(1,4):
                out[rr][c0+dx] = color
        if orient in ('v','both'):
            cc = c0+2
            for dy in range(1,4):
                out[top+dy][cc] = color
    return out