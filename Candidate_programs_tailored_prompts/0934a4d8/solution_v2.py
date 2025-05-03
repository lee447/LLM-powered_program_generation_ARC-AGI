def solve(grid):
    rows=len(grid); cols=len(grid[0])
    min_r, max_r = rows, -1
    min_c, max_c = cols, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==8:
                if r<min_r: min_r=r
                if r>max_r: max_r=r
                if c<min_c: min_c=c
                if c>max_c: max_c=c
    h = max_r-min_r+1; w = max_c-min_c+1
    band_end = min_r-1
    b = band_end
    while b>=0 and all(grid[b][c]==5 for c in range(min_c, max_c+1)):
        b-=1
    band_start = b+1
    patch_end = band_start-1
    patch_start = patch_end-h+1
    out = []
    for r in range(patch_start, patch_start+h):
        out.append(grid[r][min_c:min_c+w])
    return out