def solve(grid):
    h, w = len(grid), len(grid[0])
    for r1 in range(h):
        for c1 in range(w):
            if grid[r1][c1] == 0: continue
            for r2 in range(r1 + 1, h):
                if grid[r2][c1] == 0: continue
                for c2 in range(c1 + 1, w):
                    if grid[r1][c2] == 0 or grid[r2][c2] == 0: continue
                    ok = True
                    for c in range(c1, c2 + 1):
                        if grid[r1][c] == 0 or grid[r2][c] == 0:
                            ok = False
                            break
                    if not ok: continue
                    for r in range(r1, r2 + 1):
                        if grid[r][c1] == 0 or grid[r][c2] == 0:
                            ok = False
                            break
                    if not ok: continue
                    seeds = []
                    for c in range(c1, c2 + 1):
                        if grid[r1][c] > 1: seeds.append(grid[r1][c])
                        if grid[r2][c] > 1: seeds.append(grid[r2][c])
                    for r in range(r1 + 1, r2):
                        if grid[r][c1] > 1: seeds.append(grid[r][c1])
                        if grid[r][c2] > 1: seeds.append(grid[r][c2])
                    if not seeds: continue
                    seed = max(set(seeds), key=seeds.count)
                    for rr in range(r1 + 1, r2):
                        for cc in range(c1 + 1, c2):
                            grid[rr][cc] = seed
    return grid