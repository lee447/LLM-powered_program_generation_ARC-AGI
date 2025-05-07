def solve(grid):
    h = len(grid)
    w = len(grid[0])
    # find block-row clusters (runs of 5 non-zero rows separated by zero rows)
    nonzero = [any(cell != 0 for cell in row) for row in grid]
    clusters = []
    i = 0
    while i < h:
        if nonzero[i]:
            j = i
            while j < h and nonzero[j]:
                j += 1
            if j - i >= 5:
                clusters.append(i)
            i = j
        else:
            i += 1
    # determine mode based on cluster 1 interior
    small = True
    if len(clusters) > 1:
        cr = clusters[1]
        interior_nonzero = False
        for r in range(cr + 1, cr + 4):
            for c in range(w):
                if grid[r][c] != 0:
                    interior_nonzero = True
                    break
            if interior_nonzero:
                break
        if interior_nonzero:
            small = False
    else:
        small = True
    # copy
    out = [row[:] for row in grid]
    # fill clusters
    for idx, cr in enumerate(clusters):
        do = (small and idx == 1) or (not small and idx != 1)
        if not do:
            continue
        # detect blocks in this cluster
        row0 = grid[cr]
        c = 0
        while c < w:
            if row0[c] != 0:
                color = row0[c]
                # assume block width 5
                for interior_r in range(cr + 1, cr + 4):
                    for interior_c in range(c + 1, c + 4):
                        if grid[interior_r][interior_c] == 0:
                            if (interior_r + interior_c) % 2 == 0:
                                out[interior_r][interior_c] = color
                c += 5
            else:
                c += 1
    return out