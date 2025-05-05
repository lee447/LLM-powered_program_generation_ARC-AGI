from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = [v for v in grid[0] if v not in (0, 8)]
    pairs = list(zip(colors, colors[1:]))
    label = [[-1]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and label[i][j] < 0:
                q = deque([(i, j)])
                label[i][j] = len(comps)
                comp = []
                while q:
                    r, c = q.popleft()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 8 and label[nr][nc] < 0:
                            label[nr][nc] = label[i][j]
                            q.append((nr, nc))
                comps.append(comp)
    m = len(comps)
    info = []
    for idx, comp in enumerate(comps):
        rows = {}
        for r, c in comp:
            rows.setdefault(r, []).append(c)
        runs = {}
        for r, cs in rows.items():
            cs.sort()
            s = cs[0]
            e = cs[-1] + 1
            runs[r] = (s, e)
        top = min(runs)
        thr = runs[top][1] - runs[top][0]
        cx = sum(c for r, c in comp) / len(comp)
        info.append((idx, cx, thr, runs))
    info.sort(key=lambda x: x[1])
    mapping = {}
    plen = len(pairs)
    for pos, (idx, cx, thr, runs) in enumerate(info):
        if m > 1:
            pi = int(round(pos*(plen-1)/(m-1)))
        else:
            pi = (plen-1)//2
        left = (pos == 0 and m > 1) or m == 1 or pos*2 < m
        a, b = pairs[pi]
        if not left:
            primary, secondary = b, a
        else:
            primary, secondary = a, b
        mapping[idx] = (primary, secondary, thr, runs, left)
    out = [[0]*w for _ in range(h)]
    for idx, comp in enumerate(comps):
        primary, secondary, thr, runs, left = mapping[idx]
        for r, (s, e) in runs.items():
            L = e - s
            if L <= thr:
                col = primary
                for c in range(s, e):
                    out[r][c] = col
            else:
                rem = L - thr
                if left:
                    for c in range(s, s+thr):
                        out[r][c] = primary
                    for c in range(s+thr, e):
                        out[r][c] = secondary
                else:
                    for c in range(s, s+rem):
                        out[r][c] = secondary
                    for c in range(s+rem, e):
                        out[r][c] = primary
    return out