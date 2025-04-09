from collections import Counter
def solve(grid):
    n = len(grid)
    if n == 0:
        return grid
    m = len(grid[0])
    out = [row[:] for row in grid]
    thresh = 5
    for i in range(n):
        if sum(1 for x in out[i] if x) < thresh:
            out[i] = [0]*m
    groups = []
    i = 0
    while i < n:
        if all(x == 0 for x in out[i]):
            j = i
            while j < n and all(x == 0 for x in out[j]):
                j += 1
            groups.append((0, list(range(i, j))))
            i = j
        else:
            j = i + 1
            indices = [i]
            while j < n and any(x for x in out[j]):
                diff = sum(1 for a, b in zip(out[j], out[j-1]) if a != b)
                if diff <= 0.25 * m:
                    indices.append(j)
                    j += 1
                else:
                    break
            groups.append((1, indices))
            i = j
    for typ, rows in groups:
        if typ == 1:
            if len(rows) > 1:
                agg = []
                for col in range(m):
                    vals = [out[r][col] for r in rows]
                    cnt = Counter(vals)
                    maxfreq = max(cnt.values())
                    cands = [v for v in cnt if cnt[v] == maxfreq]
                    agg.append(min(cands))
                for r in rows:
                    out[r] = agg[:]
            for r in rows:
                newrow = out[r][:]
                for col in range(1, m-1):
                    if newrow[col] and newrow[col] != newrow[col-1] and newrow[col] != newrow[col+1] and newrow[col-1] == newrow[col+1]:
                        newrow[col] = newrow[col-1]
                out[r] = newrow
    return out