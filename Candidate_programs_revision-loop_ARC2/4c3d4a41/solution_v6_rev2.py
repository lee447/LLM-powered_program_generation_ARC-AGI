from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not vis[i][j]:
                q = deque([(i, j)])
                vis[i][j] = True
                comp = []
                while q:
                    r, c = q.popleft()
                    comp.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == 5:
                            vis[nr][nc] = True
                            q.append((nr, nc))
                clusters.append(comp)
    if len(clusters) < 2:
        return [row[:] for row in grid]
    clusters.sort(key=len)
    small, big = clusters[0], clusters[-1]
    sr = [r for r, _ in small]; sc = [c for _, c in small]
    br = [r for r, _ in big]; bc = [c for _, c in big]
    srmin, srmax = min(sr), max(sr)
    scmin, scmax = min(sc), max(sc)
    brmin, brmax = min(br), max(br)
    bcmin, bcmax = min(bc), max(bc)
    ir0, ir1 = brmin+1, brmax-1
    ic0, ic1 = bcmin+1, bcmax-1
    ih = ir1 - ir0 + 1
    iw = ic1 - ic0 + 1
    sh = srmax - srmin + 1
    sw = scmax - scmin + 1
    off_r = ir0 + (ih - sh)//2 - srmin
    off_c = ic0 + (iw - sw)//2 - scmin
    out = [row[:] for row in grid]
    for r, c in small:
        out[r][c] = 0
    for r in range(ir0, ir1+1):
        for c in range(ic0, ic1+1):
            if out[r][c] == 5:
                out[r][c] = 0
    for r, c in small:
        out[r+off_r][c+off_c] = 5
    return out