def solve(grid):
    h, w = len(grid), len(grid[0])
    def find_rings():
        rings = []
        for i in range(h-2):
            for j in range(w-2):
                b = grid[i][j]
                if b == 0: continue
                ok = True
                for x in range(3):
                    for y in range(3):
                        if x in (0,2) or y in (0,2):
                            if grid[i+x][j+y] != b: ok = False
                        elif grid[i+x][j+y] == b:
                            ok = False
                if ok:
                    rings.append((i, j, b, grid[i+1][j+1]))
        return rings

    rings = find_rings()
    if not rings:
        return [row[:] for row in grid]
    # cluster color = most frequent nonzero
    from collections import Counter
    cnt = Counter(c for row in grid for c in row if c)
    cluster = max((c for c in cnt if c!=0), key=lambda c: cnt[c])
    # bounding box of cluster
    xs = [i for i in range(h) for j in range(w) if grid[i][j]==cluster]
    ys = [j for i in range(h) for j in range(w) if grid[i][j]==cluster]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    kept = []
    removed = []
    for r in rings:
        i,j,bo,bc = r
        if any(xmin-1<=i+x<=xmax+1 and ymin-1<=j+y<=ymax+1 for x in range(3) for y in range(3)):
            removed.append(r)
        else:
            kept.append(r)
    if len(kept)!=2:
        # always keep the SE ring (max i+j) and one other with min i+j among the rest
        rings.sort(key=lambda t: t[0]+t[1])
        se = max(rings, key=lambda t: t[0]+t[1])
        others = [r for r in rings if r!=se]
        nw = min(others, key=lambda t: t[0]+t[1])
        kept = [se, nw]
        removed = [r for r in rings if r not in kept]
    # map new centers from removed rings by ascending outer color
    rem = sorted(removed, key=lambda r: r[2])
    out = [row[:] for row in grid]
    # zero out all ring borders
    for i,j,bo,bc in rings:
        for x in range(3):
            for y in range(3):
                if x in (0,2) or y in (0,2):
                    out[i+x][j+y] = 0
        out[i+1][j+1] = 0
    # restore cluster
    for i in range(h):
        for j in range(w):
            if grid[i][j]==cluster:
                out[i][j] = cluster
    # restore and set new centers for kept
    for idx,(i,j,bo,bc) in enumerate(kept):
        for x in range(3):
            for y in range(3):
                if x in (0,2) or y in (0,2):
                    out[i+x][j+y] = bo
        if len(rem)>=2:
            # map: first kept gets center of rem[1], second gets rem[0]
            nc = rem[1][3] if idx==0 else rem[0][3]
        else:
            nc = bc
        out[i+1][j+1] = nc
    return out