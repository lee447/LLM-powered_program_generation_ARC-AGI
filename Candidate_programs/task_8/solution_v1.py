def solve(grid):
    import math
    h = len(grid)
    if h==0:
        return grid
    w = len(grid[0])
    # make a deep copy of grid
    out = [row[:] for row in grid]
    # helper: frequency of non‐zero in each column
    freq = [0]*w
    for j in range(w):
        for i in range(h):
            if grid[i][j] != 0:
                freq[j] += 1
    # Determine number of “strokes” from max nonzero count in any row
    row_nonzero = [sum(1 for x in row if x!=0) for row in grid]
    expected = max(row_nonzero) if row_nonzero else 0
    if expected < 1:
        expected = 1
    # Candidate columns: those with freq>=3 and that are blank in first row.
    candidates = [j for j in range(w) if freq[j] >= 3 and grid[0][j] == 0]
    candidates.sort()
    # If no candidate exists, use the column with maximum freq.
    if not candidates:
        maxj = max(range(w), key=lambda j: freq[j])
        candidates = [maxj]
    # If more candidates than expected strokes, choose a subset.
    if len(candidates) > expected:
        if expected == 3 and len(candidates) >= 3:
            active = [candidates[0], candidates[1], candidates[-2]]
        elif expected == 2 and len(candidates) >= 2:
            active = candidates[:2]
        elif expected == 1:
            active = [candidates[0]]
        else:
            # if expected > number of candidates, use all candidates.
            active = candidates
    else:
        active = candidates
    active = sorted(active)
    # For each active column, compute the list of seed rows and do forward fill:
    for j in active:
        seeds = [(i, grid[i][j]) for i in range(h) if grid[i][j] != 0]
        if not seeds:
            continue
        # For each row i from 0 to h-1, find first seed with row index >= i;
        # if none, use the last seed.
        si = 0
        for i in range(h):
            # advance si if next seed row is before i
            while si < len(seeds) and seeds[si][0] < i:
                si += 1
            if si < len(seeds):
                fill_val = seeds[si][1]
            else:
                fill_val = seeds[-1][1]
            out[i][j] = fill_val
    return out

if __name__=="__main__":
    import json,sys
    data = sys.stdin.read()
    if data.strip()=="":
        sys.exit(0)
    grid = json.loads(data)
    res = solve(grid)
    sys.stdout.write(json.dumps(res))