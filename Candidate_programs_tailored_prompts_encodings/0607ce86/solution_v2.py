def solve(grid):
    h, w = len(grid), len(grid[0])
    non_green = [sum(1 for v in row if v != 0 and v != 3) for row in grid]
    mx = max(non_green)
    thr = mx / 2.0
    seg_rows = [i for i, c in enumerate(non_green) if c >= thr]
    segments = []
    i = 0
    while i < len(seg_rows):
        start = seg_rows[i]
        j = i
        while j + 1 < len(seg_rows) and seg_rows[j + 1] == seg_rows[j] + 1:
            j += 1
        segments.append((seg_rows[i], seg_rows[j]))
        i = j + 1
    proto_start, proto_end = segments[0]
    proto_h = proto_end - proto_start + 1
    cleaned = []
    for dr in range(proto_h):
        r = proto_start + dr
        orig = grid[r]
        row = orig[:]
        c = 0
        while c < w:
            if orig[c] == 3:
                s = c
                while c < w and orig[c] == 3:
                    c += 1
                e = c - 1
                length = e - s + 1
                if length < 2:
                    if s - 1 >= 0 and e + 1 < w and orig[s - 1] == orig[e + 1] and orig[s - 1] not in (0, 3):
                        v = orig[s - 1]
                    else:
                        v = 0
                    for x in range(s, e + 1):
                        row[x] = v
            else:
                c += 1
        cleaned.append(row)
    out = [[0]*w for _ in range(h)]
    for start, _ in segments[:3]:
        for dr in range(proto_h):
            if start + dr < h:
                out[start + dr] = cleaned[dr][:]
    return out