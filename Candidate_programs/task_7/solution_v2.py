def solve(grid):
    R, C = len(grid), len(grid[0])
    # decide new color from grid contents – new color is chosen by the occurrence of 8, then 6, then 3
    new_color = 1
    for row in grid:
        for v in row:
            if v==8:
                new_color = 8
                break
        else:
            continue
        break
    else:
        for row in grid:
            for v in row:
                if v==6:
                    new_color = 6
                    break
            else:
                continue
            break
        else:
            for row in grid:
                for v in row:
                    if v==3:
                        new_color = 3
                        break
                else:
                    continue
                break

    # find divider row indices: rows that are entirely 4
    div_rows = [i for i in range(R) if all(x==4 for x in grid[i])]
    # add boundaries at -1 and R
    row_bounds = [-1] + div_rows + [R]
    # find divider column indices: columns that are entirely 4
    div_cols = []
    for j in range(C):
        col = [grid[i][j] for i in range(R)]
        if all(x==4 for x in col):
            div_cols.append(j)
    col_bounds = [-1] + div_cols + [C]

    # copy grid
    new_grid = [row[:] for row in grid]
    # Determine grid type by new_color (8-> type 1, 6-> type 2, 3-> type 3)
    if new_color==8:
        typ = 1
    elif new_color==6:
        typ = 2
    elif new_color==3:
        typ = 3
    else:
        typ = 0

    # function to process one block (given by row indices r0+1...r1-1 and col indices c0+1...c1-1)
    def process_block(r0, r1, c0, c1):
        # block indices in grid: rows r0+1 to r1-1 and cols c0+1 to c1-1.
        block_rows = list(range(r0+1, r1))
        block_cols = list(range(c0+1, c1))
        if not block_rows or not block_cols:
            return
        bH = len(block_rows)
        # process each row in this block using different rules for non‐last and last row
        for bi, r in enumerate(block_rows):
            # gather positions (in block coordinates) where cell equals 1.
            ones = []
            for ci, c in enumerate(block_cols):
                if grid[r][c]==1:
                    ones.append(ci)
            if bi != bH-1:
                if typ==1:
                    # type1: if row is even, if count>=2 replace first and last, if count==1 replace that one;
                    # if row is odd, replace all.
                    if bi % 2 == 0:
                        if len(ones) == 1:
                            ones_to_change = ones
                        elif len(ones) >= 2:
                            ones_to_change = [ones[0], ones[-1]]
                        else:
                            ones_to_change = []
                    else:
                        ones_to_change = ones
                elif typ==2:
                    # type2: replace all 1's in non‐last rows
                    ones_to_change = ones
                elif typ==3:
                    # type3: if row is even, replace first and last if available (or the only one);
                    # if row is odd, replace only the right‐most one.
                    if bi % 2 == 0:
                        if len(ones)==0: 
                            ones_to_change = []
                        elif len(ones)==1:
                            ones_to_change = ones
                        else:
                            ones_to_change = [ones[0], ones[-1]]
                    else:
                        ones_to_change = [ones[-1]] if ones else []
                else:
                    ones_to_change = ones
            else:
                # last row in block: if there is at least one 1 and the row has odd count then change its middle one
                if len(ones) >= 3:
                    mid = ones[len(ones)//2]
                    ones_to_change = [mid]
                else:
                    ones_to_change = []
            for ci in ones_to_change:
                new_grid[r][block_cols[ci]] = new_color

    # iterate over blocks defined by adjacent boundaries
    for i in range(len(row_bounds)-1):
        for j in range(len(col_bounds)-1):
            process_block(row_bounds[i], row_bounds[i+1], col_bounds[j], col_bounds[j+1])
    return new_grid

if __name__=="__main__":
    import sys, json
    data = json.load(sys.stdin)
    grid = data["grid"]
    sol = solve(grid)
    json.dump(sol, sys.stdout)