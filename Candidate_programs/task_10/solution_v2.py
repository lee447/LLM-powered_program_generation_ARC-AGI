def solve(grid):
    import copy
    res = copy.deepcopy(grid)
    R, C = len(grid), len(grid[0])
    # find overall bounding box of nonzero cells
    rmin = R
    rmax = -1
    cmin = C
    cmax = -1
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 0:
                if r < rmin: rmin = r
                if r > rmax: rmax = r
                if c < cmin: cmin = c
                if c > cmax: cmax = c
    # helper: determine if a cell is border of the figure (4-neighbors outside bbox or 0)
    def is_border(r, c):
        if grid[r][c] == 0:
            return False
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr, nc = r+dr, c+dc
            if nr < rmin or nr > rmax or nc < cmin or nc > cmax or grid[nr][nc] == 0:
                return True
        return False
    # mark border rows inside the bbox
    border_rows = [False]*R
    for r in range(rmin, rmax+1):
        full = True
        for c in range(cmin, cmax+1):
            if grid[r][c] != 0 and is_border(r,c):
                full = False
                break
        # if none of the colored cells in the row are border cells, mark row as internal
        border_rows[r] = (not full)
    # Identify contiguous segments (by row) in the bbox that are not border rows.
    segments = []
    seg = []
    for r in range(rmin+1, rmax):
        # A row is treated as "segment row" if it has any non‐zero cell in the figure that is not a border cell.
        rowHasInternal = False
        for c in range(cmin, cmax+1):
            if grid[r][c] != 0 and (not is_border(r, c)):
                rowHasInternal = True
                break
        if rowHasInternal:
            seg.append(r)
        else:
            if seg:
                segments.append(seg)
                seg = []
    if seg:
        segments.append(seg)
    # For each segment, compute a cyclic shifting pattern.
    # Based on the training examples, the shift amount for each row is either -1, 0 or +1.
    # In a segment with length L>=3, use pattern: row0: shift left, row1: no shift, row2: shift right, row3: no, row4: shift left, etc.
    # In a segment with L==2, alternate based on the segment's index: even-index segments use [shift left, no shift] and odd-index segments use [no shift, shift left].
    for si, seg in enumerate(segments):
        L = len(seg)
        shifts = {}
        if L >= 3:
            for i, r in enumerate(seg):
                if i % 2 == 0:
                    shifts[r] = -1 if (i//2) % 2 == 0 else 1
                else:
                    shifts[r] = 0
        else:
            if si % 2 == 0:
                shifts[seg[0]] = -1
                shifts[seg[1]] = 0
            else:
                shifts[seg[0]] = 0
                shifts[seg[1]] = -1
        # apply shift for each row in seg over its internal columns (cmin+1 to cmax-1)
        for r in seg:
            s = shifts[r]
            # get indices of internal colored cells (non-border cells) in row r
            cols = [c for c in range(cmin+1, cmax) if grid[r][c] != 0 and (not is_border(r, c))]
            if not cols: continue
            newrow = res[r][:]
            for c in cols:
                newcol = c + s
                if newcol < cmin+1 or newcol >= cmax:
                    newcol = c
                newrow[newcol] = grid[r][c]
                if s != 0:
                    newrow[c] = 0
            res[r] = newrow
    return res