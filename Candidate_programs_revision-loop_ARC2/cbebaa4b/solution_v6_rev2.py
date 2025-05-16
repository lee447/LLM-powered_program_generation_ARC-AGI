from collections import deque, Counter, defaultdict

def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not vis[y][x]:
                col = grid[y][x]
                q = deque([(x,y)])
                vis[y][x] = True
                cells = []
                while q:
                    cx, cy = q.popleft()
                    cells.append((cx, cy))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < w and 0 <= ny < h and not vis[ny][nx] and grid[ny][nx] != 0:
                            vis[ny][nx] = True
                            q.append((nx, ny))
                cols = [grid[cy][cx] for cx, cy in cells]
                border = Counter(cols).most_common(1)[0][0]
                accs = [c for c in cols if c != border]
                accent = Counter(accs).most_common(1)[0][0] if accs else None
                xs = [cx for cx, cy in cells]
                ys = [cy for cx, cy in cells]
                xmin, xmax = min(xs), max(xs)
                ymin, ymax = min(ys), max(ys)
                mask = {(cx-xmin, cy-ymin): grid[cy][cx] for cx, cy in cells}
                comps.append({
                    "border": border,
                    "accent": accent,
                    "bbox": (xmin, ymin, xmax, ymax),
                    "mask": mask
                })
    by_border = defaultdict(list)
    for i, c in enumerate(comps):
        by_border[c["border"]].append(i)
    nxt = {}
    prev = set()
    for i, c in enumerate(comps):
        a = c["accent"]
        if a is not None and a in by_border:
            cand = by_border[a]
            sel = None
            cx0 = (c["bbox"][0] + c["bbox"][2])//2
            cy0 = (c["bbox"][1] + c["bbox"][3])//2
            for j in cand:
                x0, y0, x1, y1 = comps[j]["bbox"]
                if x0 <= cx0 <= x1 and y0 <= cy0 <= y1:
                    sel = j
                    break
            if sel is None:
                sel = cand[0]
            nxt[i] = sel
            prev.add(sel)
    starts = [i for i in range(len(comps)) if i not in prev]
    chains = []
    for s in starts:
        chain = []
        cur = s
        while cur is not None and cur not in chain:
            chain.append(cur)
            cur = nxt.get(cur)
        chains.append(chain)
    chains.sort(key=lambda ch: sum(comps[i]["bbox"][0] + comps[i]["bbox"][2] for i in ch) / (2*len(ch)))
    k = len(chains)
    chain_widths = [max(comps[j]["bbox"][2] - comps[j]["bbox"][0] + 1 for j in ch) for ch in chains]
    gaps = k + 1
    space = w - sum(chain_widths)
    gap_size = space // gaps if gaps > 0 else 0
    rem = space - gap_size * gaps
    gap_list = [gap_size + (1 if i < rem else 0) for i in range(gaps)]
    col_starts = []
    x = gap_list[0]
    for idx, ch in enumerate(chains):
        col_starts.append(x)
        x += chain_widths[idx] + gap_list[idx+1]
    out = [[0]*w for _ in range(h)]
    for idx, ch in enumerate(chains):
        startx = col_starts[idx]
        total_h = sum(comps[j]["bbox"][3] - comps[j]["bbox"][1] + 1 for j in ch)
        starty = max((h - total_h)//2, 0)
        y0 = starty
        for j in ch:
            xmin, ymin, xmax, ymax = comps[j]["bbox"]
            bh = ymax - ymin + 1
            for (dx, dy), col in comps[j]["mask"].items():
                xx, yy = startx + dx, y0 + dy
                if 0 <= xx < w and 0 <= yy < h:
                    out[yy][xx] = col
            y0 += bh
    return out