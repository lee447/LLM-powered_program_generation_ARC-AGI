import numpy as np

def solve(grid):
    R, C = len(grid), len(grid[0])
    g = np.array(grid)
    color = int(g[g != 0][0])
    H = []
    horiz_runs = {}
    for r in range(R):
        row = g[r]
        runs = []
        c = 0
        while c < C:
            if row[c] == color:
                start = c
                while c + 1 < C and row[c + 1] == color:
                    c += 1
                runs.append((start, c))
            c += 1
        if any(end > start for start, end in runs):
            H.append(r)
            horiz_runs[r] = runs
    H.sort()
    V = []
    vert_runs = {}
    for c in range(C):
        col = g[:, c]
        runs = []
        r = 0
        while r < R:
            if col[r] == color:
                start = r
                while r + 1 < R and col[r + 1] == color:
                    r += 1
                runs.append((start, r))
            r += 1
        if any(end > start for start, end in runs):
            V.append(c)
            vert_runs[c] = runs
    V.sort()
    out = np.zeros_like(g)
    # horizontal walls
    multi = any(len(runs) > 1 for runs in horiz_runs.values())
    for i, r in enumerate(H):
        runs = horiz_runs[r]
        c0 = min(s for s, e in runs)
        c1 = max(e for s, e in runs)
        if not multi:
            shift = i % 2
        else:
            shift = 0
        for c in range(c0, c1 + 1):
            nc = c + shift
            if 0 <= nc < C:
                out[r, nc] = color
    # vertical walls
    wave = [-1, 0, 1, 0]
    for c in V:
        for (r0, r1) in vert_runs[c]:
            # find which sandwich this run lives in
            for i in range(len(H) - 1):
                if H[i] < r0 and r1 < H[i + 1]:
                    base = H[i] + 1
                    length = r1 - r0 + 1
                    for d in range(length):
                        r = r0 + d
                        shift = wave[d % 4]
                        nc = c + shift
                        if 0 <= nc < C:
                            out[r, nc] = color
                    break
    return out.tolist()