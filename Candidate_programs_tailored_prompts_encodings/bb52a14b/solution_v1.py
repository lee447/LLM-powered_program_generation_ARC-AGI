def solve(grid):
    h = len(grid)
    w = len(grid[0])
    anchors = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] in (1,8):
                anchors.add((r,c))
    res = [row[:] for row in grid]
    vert = []
    for i in range(h-2):
        for j in range(w):
            if grid[i][j]==1 and grid[i+1][j]==4 and grid[i+2][j]==1:
                vert.append((i,j))
    for i,j in vert:
        offs = [0,1,2]
        vals = [1,4,1]
        for k in range(1, h//3+2):
            block = [i - 3*k + o for o in offs]
            if min(block) < 0: break
            if any((r,j) in anchors for r in block): break
            for idx,r in enumerate(block):
                res[r][j] = vals[idx]
        for k in range(1, h//3+2):
            block = [i + 3*k + o for o in offs]
            if max(block) >= h: break
            if any((r,j) in anchors for r in block): break
            for idx,r in enumerate(block):
                res[r][j] = vals[idx]
    crosses = []
    for i in range(h-2):
        for j in range(w-2):
            if (grid[i][j]==4 and grid[i][j+1]==8 and grid[i][j+2]==4 and
                grid[i+1][j]==8 and grid[i+1][j+1]==1 and grid[i+1][j+2]==8 and
                grid[i+2][j]==4 and grid[i+2][j+1]==8 and grid[i+2][j+2]==4):
                crosses.append((i,j))
    for i,j in crosses:
        for row in (i, i+2):
            pattern = [grid[row][j+k] for k in range(3)]
            # left
            for k in range(1, w//3+2):
                nj = j - 3*k
                if nj < 0: break
                cols = [nj, nj+1, nj+2]
                if any((row,c) in anchors for c in cols): break
                for idx,c in enumerate(cols):
                    res[row][c] = pattern[idx]
            # right
            for k in range(1, w//3+2):
                nj = j + 3*k
                if nj+2 >= w: break
                cols = [nj, nj+1, nj+2]
                if any((row,c) in anchors for c in cols): break
                for idx,c in enumerate(cols):
                    res[row][c] = pattern[idx]
    return res