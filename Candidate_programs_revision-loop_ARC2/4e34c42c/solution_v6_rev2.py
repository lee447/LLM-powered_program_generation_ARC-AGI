from collections import Counter, deque

def solve(grid):
    H, W = len(grid), len(grid[0])
    cnt = Counter(x for row in grid for x in row)
    bg = cnt.most_common(1)[0][0]
    rows = [r for r in range(H) if any(grid[r][c] != bg for c in range(W))]
    segs = []
    for r in rows:
        if not segs or r > segs[-1][1] + 1:
            segs.append([r, r])
        else:
            segs[-1][1] = r
    heights = [b - a + 1 for a, b in segs]
    hcnt = Counter(heights)
    target_h = max(h for h, c in hcnt.items() if c >= 2)
    chosen = [seg for seg, h in zip(segs, heights) if h == target_h]
    chosen.sort(key=lambda x: x[0])
    (r1, r2), (r3, r4) = chosen[0], chosen[1]
    def comp_cols(r1, r2):
        vis = [[False]*W for _ in range(H)]
        boxes = []
        for r in range(r1, r2+1):
            for c in range(W):
                if grid[r][c] != bg and not vis[r][c]:
                    q = deque([(r,c)])
                    vis[r][c] = True
                    min_r, max_r, min_c, max_c = r, r, c, c
                    while q:
                        rr, cc = q.popleft()
                        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = rr+dr, cc+dc
                            if r1 <= nr <= r2 and 0 <= nc < W and grid[nr][nc] != bg and not vis[nr][nc]:
                                vis[nr][nc] = True
                                q.append((nr, nc))
                                min_r = min(min_r, nr); max_r = max(max_r, nr)
                                min_c = min(min_c, nc); max_c = max(max_c, nc)
                    if max_c - min_c > 0:
                        boxes.append((min_c, max_c))
        cols = set()
        for mn, mx in boxes:
            for c in range(mn, mx+1):
                cols.add(c)
        return sorted(cols)
    cols_top = comp_cols(r1, r2)
    cols_bot = comp_cols(r3, r4)
    h_top = r2 - r1 + 1
    h_bot = r4 - r3 + 1
    Hout = max(h_top, h_bot)
    pad_top = (Hout - h_top) // 2
    pad_bot = (Hout - h_bot) // 2
    out = []
    for i in range(Hout):
        row = []
        rb = r3 + i - pad_bot
        if r3 <= rb <= r4:
            row += [grid[rb][c] for c in cols_bot]
        else:
            row += [bg] * len(cols_bot)
        rt = r1 + i - pad_top
        if r1 <= rt <= r2:
            row += [grid[rt][c] for c in cols_top]
        else:
            row += [bg] * len(cols_top)
        out.append(row)
    return out