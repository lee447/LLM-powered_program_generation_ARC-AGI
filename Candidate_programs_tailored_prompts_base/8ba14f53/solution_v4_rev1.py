def solve(grid):
    h, w = len(grid), len(grid[0])
    cols_nonzero = [i for i in range(w) if any(grid[r][i] != 0 for r in range(h))]
    groups = []
    start = last = None
    for i in cols_nonzero:
        if start is None:
            start = last = i
        elif i == last + 1:
            last = i
        else:
            groups.append(list(range(start, last+1)))
            start = last = i
        last = i
    if start is not None:
        groups.append(list(range(start, last+1)))
    colsA, colsB = groups[0], groups[1]
    rowsA = [r for r in range(h) if any(grid[r][c] != 0 for c in colsA)]
    rowsB = [r for r in range(h) if grid[r][colsB[0]] != 0 and grid[r][colsB[-1]] != 0]
    def make_ribbonA():
        wA, hA = len(colsA), len(rowsA)
        if wA > 3:
            r = rowsA[0]
            return [grid[r][c] for c in colsA[:3]]
        else:
            mids = rowsA[1:-1]
            k = len(mids)
            ribbon = [grid[mids[i]][colsA[0]] for i in range(k)]
            return (ribbon + [0,0,0])[:3]
    def make_ribbonB():
        wB, hB = len(colsB), len(rowsB)
        vertical = (wB == 3 or hB == 3)
        if vertical:
            if wB == 3 and hB == 3:
                mid = rowsB[hB//2]
                return [grid[mid][colsB[0]], 0, 0]
            else:
                top = grid[rowsB[0]][colsB[0]]
                bot = grid[rowsB[-1]][colsB[0]]
                return [top, bot, 0]
        else:
            if all(grid[rowsB[-1]][c] != 0 for c in colsB):
                r = rowsB[-1]
            else:
                r = rowsB[0]
            return [grid[r][c] for c in colsB[:3]]
    ribbonA = make_ribbonA()
    ribbonB = make_ribbonB()
    out = [[0]*3 for _ in range(3)]
    out[0] = ribbonA
    verticalB = (len(colsB) == 3 or len(rowsB) == 3)
    rep = 1 if verticalB else max(1, len(rowsB)-2)
    for i in range(rep):
        if 1+i < 3:
            out[1+i] = ribbonB
    return out