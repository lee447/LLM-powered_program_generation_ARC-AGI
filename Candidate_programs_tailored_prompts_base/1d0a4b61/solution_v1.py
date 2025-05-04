def solve(grid):
    H, W = len(grid), len(grid[0])
    interior = list(range(1, H-1))
    mask_rows = [r for r in interior if any(grid[r][c]==0 for c in range(1, W-1))]
    nonmask_rows = [r for r in interior if all(grid[r][c]!=0 for c in range(1, W-1))]
    seg = {r: grid[r][1:W-1] for r in nonmask_rows}
    p = 1
    while True:
        ok = True
        for r in nonmask_rows:
            k = r + p
            if k in seg and seg[r] != seg[k]:
                ok = False
                break
        if ok:
            break
        p += 1
    for r in mask_rows:
        m = r % p
        for t in nonmask_rows:
            if t % p == m:
                grid[r][1:W-1] = seg[t][:]
                break
    return grid