from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                comp = []
                stack = [(i,j)]
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not seen[nr][nc]:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                clusters.append(comp)
    best = max(clusters, key=lambda comp: (len(comp), min(c for _,c in comp)))
    rows = [r for r,_ in best]
    cols = [c for _,c in best]
    rmin, rmax = min(rows), max(rows)
    cmin, cmax = min(cols), max(cols)
    stripe_rows = []
    for r in range(rmin, rmax+1):
        run = 0
        mx = 0
        for c in range(cmin, cmax+1):
            if grid[r][c] == 4:
                run += 1
                mx = max(mx, run)
            else:
                run = 0
        if mx >= 4:
            stripe_rows.append(r)
    hbox = rmax - rmin + 1
    if stripe_rows:
        fb = 0
    else:
        if hbox > 12:
            stripe_rows = [rmin, (rmin+rmax)//2, rmax]
            fb = 1
        elif hbox <= 6:
            stripe_rows = [rmin, rmax]
            fb = 3
        else:
            step = (rmax - rmin) // 3
            stripe_rows = [rmin, rmin+step, rmin+2*step, rmax]
            fb = 2
    stripe_rows = sorted(set(stripe_rows))
    H = len(stripe_rows)
    W = cmax - cmin + 1
    out = [[0]*W for _ in range(H)]
    for i,r in enumerate(stripe_rows):
        out[i][0] = 8
        out[i][W-1] = 8
        if fb == 0:
            segs = []
            run = 0
            for c in range(cmin, cmax+1):
                if grid[r][c] == 4:
                    run += 1
                else:
                    if run >= 4:
                        segs.append((c-run, c-1))
                    run = 0
            if run >= 4:
                segs.append((cmax-run+1, cmax))
            for a,b in segs:
                out[i][a-cmin] = 8
                out[i][b-cmin] = 8
            runs2 = []
            run = 0
            for c in range(cmin, cmax+1):
                if grid[r][c] != 0 and grid[r][c] != 4:
                    run += 1
                else:
                    if run >= 2:
                        runs2.append((c-run, c-1))
                    run = 0
            if run >= 2:
                runs2.append((c-run, c-1))
            for a,b in runs2:
                out[i][a-cmin] = 8
                out[i][b-cmin] = 8
        elif fb == 1:
            if i == 1:
                run = 0
                runs2 = []
                for c in range(cmin, cmax+1):
                    if grid[r][c] != 0 and grid[r][c] != 4:
                        run += 1
                    else:
                        if run >= 2:
                            runs2.append((c-run, c-1))
                        run = 0
                if run >= 2:
                    runs2.append((c-run, c-1))
                for a,b in runs2:
                    out[i][a-cmin] = 8
                    out[i][b-cmin] = 8
        elif fb == 2:
            if i > 0:
                run = 0
                runs2 = []
                for c in range(cmin, cmax+1):
                    if grid[r][c] != 0 and grid[r][c] != 4:
                        run += 1
                    else:
                        if run >= 2:
                            runs2.append((c-run, c-1))
                        run = 0
                if run >= 2:
                    runs2.append((c-run, c-1))
                for a,b in runs2:
                    out[i][a-cmin] = 8
                    out[i][b-cmin] = 8
        else:
            run = 0
            segs = []
            for c in range(cmin, cmax+1):
                if grid[r][c] == 4:
                    run += 1
                else:
                    if run >= 3:
                        segs.append((c-run, c-1))
                    run = 0
            if run >= 3:
                segs.append((cmax-run+1, cmax))
            for a,b in segs:
                out[i][a-cmin] = 8
                out[i][b-cmin] = 8
    return out