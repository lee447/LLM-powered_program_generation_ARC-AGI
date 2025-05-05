def solve(grid):
    h = len(grid)
    w = len(grid[0])
    nonzeros = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0]
    rs = [r for r,_,_ in nonzeros]
    cs = [c for _,c,_ in nonzeros]
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    hr_sum = min_r+max_r
    hc_sum = min_c+max_c
    horiz = hr_sum%2==0 and all(grid[hr_sum-r][c]==v for r,c,v in nonzeros)
    vert = hc_sum%2==0 and all(grid[r][hc_sum-c]==v for r,c,v in nonzeros)
    res = [row[:] for row in grid]
    if horiz:
        ar = hr_sum//2
        for c in range(w):
            res[ar][c] = 3
    elif vert:
        ac = hc_sum//2
        for r in range(h):
            res[r][ac] = 3
    return res