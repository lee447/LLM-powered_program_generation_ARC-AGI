def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # detect which task by unique colors present
    s = set(x for row in grid for x in row)
    # TRAIN1: background=1, special colors {4,8,2}
    if 4 in s:
        # blocks are 4×4 separated by one-zero lines
        for br in range((h - 1) // 5 + 1):
            r0 = br * 5 + 1
            for bc in range((w - 1) // 5 + 1):
                c0 = bc * 5 + 1
                # skip the second block‐row (index 1)
                if br == 1: continue
                rr, cc = r0 + 2, c0 + 2
                if out[rr][cc] != 2:
                    out[rr][cc] = 2
    # TRAIN2: background=2, special colors among {1,3,6,8}
    elif 6 in s:
        for br in range((h - 1) // 5 + 1):
            r0 = br * 5 + 1
            for bc in range((w - 1) // 5 + 1):
                c0 = bc * 5 + 1
                # skip block‐row 1
                if br == 1: continue
                # skip last block‐col
                if bc == ((w - 1) // 5): continue
                # look at interior 2×2 at top‐left of center
                r1, c1 = r0 + 1, c0 + 1
                v = grid[r1][c1]
                # target just below that
                rr, cc = r1 + 1, c1
                # rotate among {1,3,6,8} in appearance order
                cycle = [1, 3, 6, 8]
                if v in cycle:
                    out[rr][cc] = cycle[(cycle.index(v) + 1) % len(cycle)]
    # TRAIN3: background=8, special colors among {4,7}
    else:
        for br in range((h - 1) // 5 + 1):
            r0 = br * 5 + 1
            for bc in range((w - 1) // 5 + 1):
                c0 = bc * 5 + 1
                # skip block‐rows 0 and 1
                if br < 2: continue
                # skip first block‐col
                if bc == 0: continue
                r1, c1 = r0 + 1, c0 + 1
                v = grid[r1][c1]
                rr, cc = r1 + 1, c1
                # map 4→3, 7→4
                if v == 4:
                    out[rr][cc] = 3
                elif v == 7:
                    out[rr][cc] = 4
    return out