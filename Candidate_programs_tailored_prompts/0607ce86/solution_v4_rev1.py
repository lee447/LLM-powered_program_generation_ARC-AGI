def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    bands = []
    zrow = [0]*w
    in_band = False
    for r in range(h):
        if not in_band and any(grid[r][c] != 0 for c in range(w)):
            start = r
            in_band = True
        if in_band and all(grid[r][c] == 0 for c in range(w)):
            bands.append((start, r-1))
            in_band = False
    if in_band:
        bands.append((start, h-1))
    for start, end in bands:
        rows = list(range(start, end+1))
        cnt = [0]*w
        for c in range(w):
            for r in rows:
                if grid[r][c] != 0:
                    cnt[c] += 1
        mask = [cnt[c] > (end-start+1)/2 for c in range(w)]
        # split mask into contiguous segments
        segs = []
        c = 0
        while c < w:
            if mask[c]:
                j = c
                while j < w and mask[j]:
                    j += 1
                segs.append(list(range(c, j)))
                c = j
            else:
                c += 1
        for seg in segs:
            # collect rows that carry this segment
            rows_seg = [r for r in rows if any(grid[r][c] != 0 for c in seg)]
            # group by pattern on this segment
            groups = {}
            for r in rows_seg:
                key = tuple(grid[r][c] for c in seg)
                groups.setdefault(key, []).append(r)
            # find majority key
            maj_key = max(groups.items(), key=lambda x: len(x[1]))[0]
            for r in rows_seg:
                for i, c in enumerate(seg):
                    out[r][c] = maj_key[i]
    return out