from collections import deque, Counter, defaultdict
import math

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
                freq = Counter(cols)
                border = freq.most_common(1)[0][0]
                acc = [c for c in cols if c != border]
                accent = Counter(acc).most_common(1)[0][0] if acc else None
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
    by_border = {c["border"]: i for i, c in enumerate(comps)}
    nxt = {}
    inv = defaultdict(list)
    for i, c in enumerate(comps):
        b, a = c["border"], c["accent"]
        if a is not None and a in by_border:
            nxt[i] = by_border[a]
            inv[by_border[a]].append(i)
    starts = [i for i,c in enumerate(comps) if i not in nxt.values()]
    chains = []
    for s in sorted(starts):
        chain = []
        cur = s
        while cur is not None and cur not in chain:
            chain.append(cur)
            cur = nxt.get(cur)
        chains.append(chain)
    chains.sort(key=lambda ch: sum((c := comps[i])["bbox"][0] + c["bbox"][2] for i in ch)/ (2*len(ch)))
    total_cw = sum(max(c["bbox"][2]-c["bbox"][0]+1 for i in ch for c in [comps[i]]) for ch in chains)
    k = len(chains)
    gaps = k+1
    space = w - total_cw
    gap_size = space//gaps if gaps>0 else 0
    rem = space - gap_size*gaps
    gap_list = [gap_size + (1 if i<rem else 0) for i in range(gaps)]
    col_starts = []
    x = gap_list[0]
    for i,ch in enumerate(chains):
        col_starts.append(x)
        cw = max(comps[i]["bbox"][2]-comps[i]["bbox"][0]+1 for i in ch for _ in [0])
        x += cw + gap_list[i+1]
    out = [[0]*w for _ in range(h)]
    for i,ch in enumerate(chains):
        startx = col_starts[i]
        total_h = sum(comps[j]["bbox"][3]-comps[j]["bbox"][1]+1 for j in ch)
        starty = (h - total_h)//2
        y0 = starty
        for j in ch:
            xmin, ymin, xmax, ymax = comps[j]["bbox"]
            bh = ymax - ymin + 1
            for (dx, dy), col in comps[j]["mask"].items():
                out[y0+dy][startx+dx] = col
            y0 += bh
    return out