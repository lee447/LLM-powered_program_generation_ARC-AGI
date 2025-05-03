def solve(grid):
    R, C = len(grid), len(grid[0])
    # 1. find 8-block bounding box
    rows = [i for i in range(R) for j in range(C) if grid[i][j] == 8]
    cols = [j for i in range(R) for j in range(C) if grid[i][j] == 8]
    rmin, rmax = min(rows), max(rows)
    cmin, cmax = min(cols), max(cols)
    block_w = cmax - cmin + 1
    # 2. find grey‐band rows by 5‐count
    counts5 = [row.count(5) for row in grid]
    m5 = max(counts5)
    thr = (m5 + 1) // 2
    cand = [i for i, v in enumerate(counts5) if v >= thr]
    # find longest contiguous run in cand
    runs = []
    run = []
    for i in cand:
        if not run or i == run[-1] + 1:
            run.append(i)
        else:
            runs.append(run)
            run = [i]
    if run: runs.append(run)
    band = max(runs, key=len)
    band_h = len(band)
    # 3. search for a patch of size band_h×block_w with only wedge colors {1,3,4,6,7,9}
    bad = {0, 2, 5, 8}
    for i in range(R - band_h + 1):
        for j in range(C - block_w + 1):
            ok = True
            for di in range(band_h):
                for dj in range(block_w):
                    if grid[i + di][j + dj] in bad:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return [grid[i + di][j : j + block_w] for di in range(band_h)]
    return []