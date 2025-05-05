from itertools import groupby

def solve(grid):
    h, w = len(grid), len(grid[0])
    def max_runs(v):
        H = 0
        rows = []
        for r in range(h):
            cnt = 0
            for c in range(w):
                if grid[r][c] == v:
                    cnt += 1
                    H = max(H, cnt)
                else:
                    cnt = 0
            # record rows with a run of length H
        R = []
        cnts = []
        for r in range(h):
            cnt = 0
            best = 0
            for c in range(w):
                if grid[r][c] == v:
                    cnt += 1
                    if cnt > best:
                        best = cnt
                else:
                    cnt = 0
            if best == H and H > 0:
                # find leftmost start
                cnt = 0
                for c in range(w):
                    if grid[r][c] == v:
                        cnt += 1
                        if cnt == H:
                            R.append((r, c - H + 1))
                            break
                    else:
                        cnt = 0
        V = 0
        C = []
        for c in range(w):
            cnt = 0
            for r in range(h):
                if grid[r][c] == v:
                    cnt += 1
                    V = max(V, cnt)
                else:
                    cnt = 0
        for c in range(w):
            cnt = 0
            best = 0
            for r in range(h):
                if grid[r][c] == v:
                    cnt += 1
                    if cnt > best:
                        best = cnt
                else:
                    cnt = 0
            if best == V and V > 0:
                C.append(c)
        return H, R, V, C

    # gather H-V differences
    cand = []
    vals = {grid[r][c] for r in range(h) for c in range(w)}
    for v in vals:
        H, Rs, V, Cs = max_runs(v)
        if H and V:
            cand.append((H - V, v, H, Rs, V, Cs))
    cand.sort(reverse=True)
    for diff, v, H, Rs, V, Cs in cand:
        if H > V:
            hr, hstart = min(Rs)
            vr = min(Cs)
            sz = V
            br = hr + 1
            tr = br + sz
            lc = vr - sz
            rc = vr
            if br >= 0 and tr <= h and lc >= 0 and rc <= w:
                block = [row[lc:rc] for row in grid[br:tr]]
                return block[::-1]
    # fallback empty
    return []
from itertools import groupby

def solve(grid):
    h, w = len(grid), len(grid[0])
    def max_runs(v):
        H = 0
        for r in range(h):
            cnt = 0
            for c in range(w):
                if grid[r][c] == v:
                    cnt += 1
                    H = max(H, cnt)
                else:
                    cnt = 0
        rows = []
        for r in range(h):
            cnt = 0
            best = 0
            for c in range(w):
                if grid[r][c] == v:
                    cnt += 1
                    if cnt > best:
                        best = cnt
                else:
                    cnt = 0
            if best == H and H > 0:
                cnt = 0
                for c in range(w):
                    if grid[r][c] == v:
                        cnt += 1
                        if cnt == H:
                            rows.append((r, c - H + 1))
                            break
                    else:
                        cnt = 0
        V = 0
        for c in range(w):
            cnt = 0
            for r in range(h):
                if grid[r][c] == v:
                    cnt += 1
                    V = max(V, cnt)
                else:
                    cnt = 0
        cols = []
        for c in range(w):
            cnt = 0
            best = 0
            for r in range(h):
                if grid[r][c] == v:
                    cnt += 1
                    if cnt > best:
                        best = cnt
                else:
                    cnt = 0
            if best == V and V > 0:
                cols.append(c)
        return H, rows, V, cols

    vals = {grid[r][c] for r in range(h) for c in range(w)}
    candidates = []
    for v in vals:
        H, rows, V, cols = max_runs(v)
        if H and V:
            candidates.append((H - V, v, H, rows, V, cols))
    candidates.sort(reverse=True)
    for diff, v, H, rows, V, cols in candidates:
        if H > V:
            hr, _ = min(rows)
            vr = min(cols)
            sz = V
            br = hr + 1
            tr = br + sz
            lc = vr - sz
            rc = vr
            if 0 <= br < tr <= h and 0 <= lc < rc <= w:
                block = [row[lc:rc] for row in grid[br:tr]]
                return block[::-1]
    return []