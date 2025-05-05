def solve(grid):
    h, w = len(grid), len(grid[0])
    anchors = []
    for r in range(h):
        for c in range(w):
            if r + 5 <= h and c + 5 <= w:
                ok = True
                for i in (0, 4):
                    for j in range(5):
                        if grid[r + i][c + j] != 3:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                for i in range(5):
                    for j in (0, 4):
                        if grid[r + i][c + j] != 3:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue
                for i in range(1, 4):
                    for j in range(1, 4):
                        if grid[r + i][c + j] != 0:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    anchors.append((r, c))
    anchors.sort(key=lambda x: x[0])
    r0, c0 = anchors[0]
    cb = c0 + 6
    for i in range(5):
        for j in range(5):
            grid[r0 + i][cb + j] = 1
    r1, _ = anchors[1]
    r2, _ = anchors[2]
    end1 = r1 + 4
    gap = r2 - end1 - 1
    rl = end1 + 1 + (gap - 3) // 2
    cl = cb + 1
    for i in range(3):
        for j in range(3):
            if i in (0, 2) or j in (0, 2):
                grid[rl + i][cl + j] = 8
    return grid