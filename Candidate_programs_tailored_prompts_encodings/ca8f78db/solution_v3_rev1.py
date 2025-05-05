def solve(grid):
    out = []
    for row in grid:
        w = len(row)
        for L in range(1, w+1):
            cycle = [None] * L
            ok = True
            for j, v in enumerate(row):
                if v != 0:
                    k = j % L
                    if cycle[k] is None:
                        cycle[k] = v
                    elif cycle[k] != v:
                        ok = False
                        break
            if not ok:
                continue
            if all(c is not None for c in cycle):
                break
        out.append([cycle[i % L] for i in range(w)])
    return out