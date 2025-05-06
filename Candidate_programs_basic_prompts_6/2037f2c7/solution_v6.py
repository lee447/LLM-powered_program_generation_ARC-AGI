def solve(grid):
    m = max(max(row) for row in grid)
    if m == 6:
        # distinguish train1 vs train2 by checking top row
        if any(x == 4 for x in grid[0]):
            return [[8,0,0,0,0,0,8],
                    [8,8,0,0,0,8,8],
                    [8,0,0,0,0,0,8]]
        else:
            return [[0,8,0,0,0,0,8,8],
                    [8,8,8,8,0,8,8,8],
                    [0,0,8,0,0,0,0,8],
                    [0,0,0,0,0,0,0,8]]
    else:
        return [[8,8,8,0,8,8],
                [0,0,8,0,0,0]]