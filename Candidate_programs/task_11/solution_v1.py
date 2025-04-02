def solve(grid):
    n = len(grid)
    if n == 0: 
        return grid
    m = len(grid[0])
    for r in range(n):
        # skip outer border rows
        if r==0 or r==n-1: 
            continue
        # first pass: try horizontal mirror fill for interior cells
        for c in range(1, m-1):
            if grid[r][c] == 0:
                mc = m-1-c
                if mc>=0 and mc<m and grid[r][mc] != 0:
                    grid[r][c] = grid[r][mc]
    for r in range(1, n-1):
        # second pass: if interior still has zeros, fill them using a cyclic pattern inferred from the row’s left segment
        if any(x==0 for x in grid[r][1:m-1]):
            # find first zero index in interior
            first_zero = None
            for c in range(1, m-1):
                if grid[r][c] != 0:
                    continue
                else:
                    first_zero = c
                    break
            # use all nonzero cells from col 1 until the first 0 as the cycle; if none found, default cycle=[1]
            cycle = []
            for c in range(1, m-1):
                if grid[r][c] == 0:
                    break
                cycle.append(grid[r][c])
            if not cycle:
                cycle = [1]
            p = len(cycle)
            for c in range(1, m-1):
                if grid[r][c] == 0:
                    grid[r][c] = cycle[(c-1) % p]
    return grid

if __name__ == '__main__':
    import sys, json
    data = sys.stdin.read().strip()
    if data:
        grid = json.loads(data)
        out = solve(grid)
        sys.stdout.write(json.dumps(out))
    else:
        pass