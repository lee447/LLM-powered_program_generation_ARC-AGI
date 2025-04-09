import sys
from collections import Counter

def solve(grid):
    n = len(grid)
    if n==0:
        return grid
    m = len(grid[0])
    # make a copy
    out = [row[:] for row in grid]
    # threshold: if a row has fewer than 3 non‐zero cells it is considered “noise” and cleared.
    thresh = 3
    # Pre‐clean individual rows: if a row has nonzero count < thresh then clear it.
    for i in range(n):
        cnt = sum(1 for x in out[i] if x)
        if cnt < thresh:
            out[i] = [0]*m
    # Now group consecutive rows that are either all zeros or not.
    groups = []
    i = 0
    while i < n:
        typ = 0 if all(x==0 for x in out[i]) else 1
        j = i
        while j < n:
            curtype = 0 if all(x==0 for x in out[j]) else 1
            if curtype!=typ:
                break
            j += 1
        groups.append((typ, list(range(i,j))))
        i = j
    # For groups of type 1 (nonzero rows), compute column‐wise “mode” among the rows in the group.
    # In case of tie, choose the smallest nonzero. If no nonzero value appears in a column, set 0.
    for typ, rows in groups:
        if typ==1:
            agg = [0]*m
            for col in range(m):
                vals = [out[r][col] for r in rows]
                # consider only nonzero values
                nz = [v for v in vals if v]
                if nz:
                    cnt = Counter(nz)
                    maxfreq = max(cnt.values())
                    # among those with maxfreq pick smallest value
                    cand = [v for v in cnt if cnt[v]==maxfreq]
                    agg[col] = min(cand)
                else:
                    agg[col] = 0
            # assign aggregated row to every row in the group
            for r in rows:
                out[r] = agg[:]
    return out

if __name__=="__main__":
    data = sys.stdin.read().strip()
    if not data:
        exit(0)
    import json
    grid = json.loads(data)
    res = solve(grid)
    sys.stdout.write(json.dumps(res))