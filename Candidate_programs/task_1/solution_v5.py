def solve(grid):
    h = len(grid)
    if h == 0:
        return grid
    w = len(grid[0])
    newgrid = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            # set border to 0
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                newgrid[i][j] = 0
            else:
                val = grid[i][j]
                if val == 0:
                    newgrid[i][j] = 0
                else:
                    # Check if any immediate neighbor (up,down,left,right) is same.
                    same = ((grid[i][j-1] == val) or (grid[i][j+1] == val) or (grid[i-1][j] == val) or (grid[i+1][j] == val))
                    if same:
                        newgrid[i][j] = val
                    else:
                        # Check horizontal pair: if left and right exist and equal and nonzero.
                        if grid[i][j-1] == grid[i][j+1] and grid[i][j-1] != 0:
                            newgrid[i][j] = grid[i][j-1]
                        # Check vertical pair.
                        elif grid[i-1][j] == grid[i+1][j] and grid[i-1][j] != 0:
                            newgrid[i][j] = grid[i-1][j]
                        else:
                            newgrid[i][j] = 0
    return newgrid

if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        grid = json.loads(data)
        res = solve(grid)
        sys.stdout.write(json.dumps(res))
    else:
        print("[]")