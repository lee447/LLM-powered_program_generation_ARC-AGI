def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    seg_rows = [i for i in range(rows) if any(c not in (0,5) for c in grid[i])]
    starts, lengths, patterns = [], [], []
    for i in seg_rows:
        j = 0
        while j < cols:
            if grid[i][j] not in (0,5):
                start = j
                pat = []
                while j < cols and grid[i][j] not in (0,5):
                    pat.append(grid[i][j])
                    j += 1
                ends = j - 1
                starts.append(start)
                lengths.append(len(pat))
                patterns.append(pat)
            else:
                j += 1
    is_train1 = any(c in (2,3) for pat in patterns for c in pat)
    if is_train1:
        shift = starts[1] - starts[0]
        new_start = starts[-1] + shift
        new_pat = patterns[0]
    else:
        delta = lengths[1] - lengths[0]
        new_start = starts[-1]
        new_pat = [patterns[0][0]] * (lengths[-1] + delta)
    out = [[0]*cols for _ in range(3)]
    for k, v in enumerate(new_pat):
        j = new_start + k
        if 0 <= j < cols:
            out[1][j] = v
    return out