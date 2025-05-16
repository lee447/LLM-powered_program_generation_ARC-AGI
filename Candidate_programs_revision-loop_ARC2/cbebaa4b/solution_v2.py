def solve(grid):
    h = len(grid)
    w = len(grid[0])
    from collections import deque, Counter, defaultdict
    vis = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not vis[y][x]:
                col0 = grid[y][x]
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
                comps.append(cells)
    comp_info = {}
    for cells in comps:
        cols = [grid[y][x] for x,y in cells]
        freq = Counter(cols)
        border_color = freq.most_common(1)[0][0]
        acc_cols = [c for c in cols if c != border_color]
        accent_color = None
        if acc_cols:
            accent_color = Counter(acc_cols).most_common(1)[0][0]
        xs = [x for x,y in cells]
        ys = [y for x,y in cells]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        comp_info[border_color] = {
            "cells": cells,
            "border": border_color,
            "accent": accent_color,
            "bbox": (xmin, ymin, xmax, ymax),
        }
    borders = list(comp_info.keys())
    nxt = {}
    inv = defaultdict(list)
    for b in borders:
        a = comp_info[b]["accent"]
        nxt[b] = a
        if a in comp_info:
            inv[a].append(b)
    used = set()
    chains = []
    for b in borders:
        if b not in used:
            # find group by undirected connectivity
            stack = [b]
            group = set([b])
            while stack:
                u = stack.pop()
                for v in inv.get(u, []):
                    if v not in group:
                        group.add(v); stack.append(v)
                v = nxt.get(u)
                if v in comp_info and v not in group:
                    group.add(v); stack.append(v)
            # find start(s)
            starts = [u for u in group if u not in inv]
            if not starts:
                starts = [sorted(group)[0]]
            for st in sorted(starts):
                chain = []
                cur = st
                while cur in comp_info and cur not in chain:
                    chain.append(cur)
                    nc = nxt.get(cur)
                    if nc in comp_info:
                        cur = nc
                    else:
                        break
                chains.append(chain)
            used |= group
    # sort chains by input avg x
    def chain_avg_x(chain):
        s = 0; cnt = 0
        for b in chain:
            for x,y in comp_info[b]["cells"]:
                s += x; cnt += 1
        return s/cnt if cnt else 0
    chains.sort(key=chain_avg_x)
    out = [[0]*w for _ in range(h)]
    # placement
    # compute column for each chain
    col_starts = {}
    acc_w = 0
    for i,chain in enumerate(chains):
        # chain width = max bbox width
        cw = 0
        for b in chain:
            xmin,ymin,xmax,ymax = comp_info[b]["bbox"]
            cw = max(cw, xmax-xmin+1)
        # average x
        avgx = chain_avg_x(chain)
        start = int(round(avgx - cw/2))
        if start < 0: start = 0
        if start+cw > w: start = w-cw
        col_starts[i] = start
    # place blocks in each chain
    for i,chain in enumerate(chains):
        startx = col_starts[i]
        total_h = sum(comp_info[b]["bbox"][3]-comp_info[b]["bbox"][1]+1 for b in chain)
        starty = (h - total_h)//2
        y0 = starty
        for b in chain:
            xmin,ymin,xmax,ymax = comp_info[b]["bbox"]
            bh = ymax-ymin+1
            for x,y in comp_info[b]["cells"]:
                rx = x - xmin
                ry = y - ymin
                out_y = y0 + ry
                out_x = startx + rx
                out[out_y][out_x] = grid[y][x]
            y0 += bh
    return out