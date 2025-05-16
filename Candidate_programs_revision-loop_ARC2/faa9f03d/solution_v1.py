def solve(grid):
    h=len(grid); w=len(grid[0])
    orig=[row[:] for row in grid]
    colors=set(c for row in grid for c in row if c!=0)
    border=None
    for c in colors:
        for r in range(h):
            if sum(1 for x in grid[r] if x==c)==w: border=c
        for cc in range(w):
            if sum(1 for r in range(h) if grid[r][cc]==c)==h: border=c
    cand=sorted(c for c in colors if c!=border)
    for X in cand:
        for r in range(h):
            for c in range(w-2):
                if grid[r][c]==X and grid[r][c+2]==X and grid[r][c+1]!=X:
                    grid[r][c+1]=X
        for c in range(w):
            for r in range(h-2):
                if grid[r][c]==X and grid[r+2][c]==X and grid[r+1][c]!=X:
                    grid[r+1][c]=X
    if cand:
        ext=cand[-1]
        for c in range(w):
            if orig[0][c]==ext and orig[1][c]==ext and orig[2][c]==ext:
                grid[0][c]=0; grid[1][c]=0
                for r in range(3,h):
                    grid[r][c]=ext
    return grid