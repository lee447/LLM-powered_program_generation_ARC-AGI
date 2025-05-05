def solve(grid):
    h = len(grid)
    w = len(grid[0])
    rings = []
    for i in range(h - 3):
        for j in range(w - 3):
            ok = True
            for di in (1, 2):
                for dj in (1, 2):
                    if grid[i+di][j+dj] != 0:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            color = None
            for di in range(4):
                for dj in range(4):
                    if di in (0, 3) or dj in (0, 3):
                        v = grid[i+di][j+dj]
                        if v == 0:
                            ok = False
                            break
                        if color is None:
                            color = v
                        elif v != color:
                            ok = False
                            break
                if not ok:
                    break
            if not ok:
                continue
            block = [[grid[i+di][j+dj] for dj in range(4)] for di in range(4)]
            rings.append((i, j, block))
    rings.sort(key=lambda x: (x[1], x[0]))
    out = [[0] * (4 * len(rings)) for _ in range(4)]
    for idx, (_, _, block) in enumerate(rings):
        off = idx * 4
        for di in range(4):
            for dj in range(4):
                out[di][off + dj] = block[di][dj]
    return out