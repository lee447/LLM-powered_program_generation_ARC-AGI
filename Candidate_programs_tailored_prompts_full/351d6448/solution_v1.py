def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows>0 else 0
    clusters = []
    for i in range(1, rows):
        if all(grid[i][j]==5 for j in range(cols)):
            r = i-1
            j = 0
            while j<cols and grid[r][j]==0:
                j+=1
            if j<cols:
                start = j
                vals = []
                while j<cols and grid[r][j]!=0:
                    vals.append(grid[r][j])
                    j+=1
                clusters.append((r, start, vals))
    clusters.sort(key=lambda x: x[0])
    starts = [c[1] for c in clusters]
    delta = starts[1]-starts[0] if len(starts)>1 else 0
    last_start, last_vals = starts[-1], clusters[-1][2]
    new_start = last_start+delta
    out = [[0]*cols for _ in range(3)]
    for k,v in enumerate(last_vals):
        if 0<=new_start+k<cols:
            out[1][new_start+k] = v
    return out