def solve(grid):
    n = len(grid)
    m = len(grid[0])
    # find color and bounding box for nonzero cells
    c = None
    top = n; bottom = -1; left = m; right = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                if c is None:
                    c = grid[i][j]
                if i < top: top = i
                if i > bottom: bottom = i
                if j < left: left = j
                if j > right: right = j
    # if no nonzero, return copy
    if c is None:
        return [row[:] for row in grid]
    H = bottom - top + 1
    # determine shift function
    def get_shift(i):
        # i: row index within bounding box (0-indexed)
        if c in (2,3):
            if i == 0 or i == H-1:
                return 0
            # for interior rows, only odd rows shift
            if i % 2 == 1:
                # alternate: first odd gives -1, second odd gives +1, etc.
                if ((i//2) % 2) == 0:
                    return -1
                else:
                    return 1
            return 0
        elif c == 5:
            # every even row (including index0) shifts -1, odd = 0.
            return -1 if (i % 2 == 0) else 0
        elif c == 8:
            # every even row shifts alternately: if even row and (i//2) even => +1, if even and (i//2) odd => -1, odd rows 0.
            if i % 2 == 0:
                return 1 if ((i//2) % 2 == 0) else -1
            return 0
        else:
            return 0

    out = [row[:] for row in grid]
    # Process rows in bounding box only.
    for i in range(top, bottom+1):
        shift = get_shift(i - top)
        # work on a copy of the row from the input grid for segment detection.
        row = grid[i]
        segs = []
        j = 0
        while j < m:
            if row[j] == c:
                start = j
                while j < m and row[j] == c:
                    j += 1
                end = j - 1
                segs.append((start, end))
            else:
                j += 1
        # Remove original c's from this row
        newrow = out[i][:]
        for (s,e) in segs:
            for j in range(s, e+1):
                newrow[j] = 0
        # Place them shifted
        for (s,e) in segs:
            ns = s + shift
            ne = e + shift
            # fill contiguous block from ns to ne if in bounds
            for j in range(ns, ne+1):
                if 0 <= j < m:
                    newrow[j] = c
        out[i] = newrow
    return out

if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        grid = json.loads(data)
        out_grid = solve(grid)
        sys.stdout.write(json.dumps(out_grid))
    else:
        pass