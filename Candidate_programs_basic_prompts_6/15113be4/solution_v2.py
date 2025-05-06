def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_c = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    sep_r = [i for i in range(h) if all(grid[i][j] == 4 for j in range(w))]
    col_bounds = []
    prev = -1
    for c in sep_c + [w]:
        if c - prev - 1 > 0:
            col_bounds.append((prev + 1, c))
        prev = c
    row_bounds = []
    prev = -1
    for r in sep_r + [h]:
        if r - prev - 1 > 0:
            row_bounds.append((prev + 1, r))
        prev = r
    nb_r, nb_c = len(row_bounds), len(col_bounds)
    fill = next((col for row in grid for col in row if col not in (0,1,4)), None)
    if fill is None:
        fill = 8
    for br in range(nb_r):
        r0, r1 = row_bounds[br]
        for bc in range(nb_c):
            c0, c1 = col_bounds[bc]
            block = [grid[i][c0:c1] for i in range(r0, r1)]
            flat = sum(block, [])
            if flat.count(fill) == 0:
                cnt1 = flat.count(1)
                cnt0 = flat.count(0)
                if cnt1 == 3:
                    for (i,j) in ((0,0),(0,2),(1,1)):
                        grid[r0+i][c0+j] = fill
                elif cnt0 == 3:
                    for (i,j) in ((0,2),(1,0),(1,1),(2,1)):
                        grid[r0+i][c0+j] = fill
                else:
                    for (i,j) in ((0,1),(1,0),(1,1),(1,2),(2,1)):
                        if grid[r0+i][c0+j] != 4:
                            grid[r0+i][c0+j] = fill
    return grid