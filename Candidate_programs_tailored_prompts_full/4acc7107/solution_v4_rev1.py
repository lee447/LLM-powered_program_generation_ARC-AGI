from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    pos = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                pos.setdefault(v, []).append((r,c))
    clusters = {}
    for v, pts in pos.items():
        spts = set(pts)
        visited = set()
        cls = []
        for p in pts:
            if p in visited: continue
            q = deque([p])
            comp = []
            visited.add(p)
            while q:
                x,y = q.popleft()
                comp.append((x,y))
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if (nx,ny) in spts and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            cls.append(comp)
        clusters[v] = cls
    colors = sorted(clusters.keys(), key=lambda v: min(c for r,c in pos[v]))
    out = [[0]*W for _ in range(H)]
    curx = 0
    for v in colors:
        cls = clusters[v]
        boxes = []
        for comp in cls:
            rs = [r for r,c in comp]
            cs = [c for r,c in comp]
            h = max(rs)-min(rs)+1
            w = max(cs)-min(cs)+1
            boxes.append((h,w,comp,min(rs),min(cs)))
        a,b = boxes
        if a[0]>b[0] or (a[0]==b[0] and (a[1]>b[1] or (a[1]==b[1] and len(a[2])>len(b[2])))):
            big, small = a, b
        else:
            big, small = b, a
        h_s,w_s,comp_s,min_rs,min_cs = small
        h_b,w_b,comp_b,min_rb,min_cb = big
        gap = 1
        bh = h_s + gap + h_b
        start_r = H - bh
        shift_s_r = start_r - min_rs
        shift_b_r = start_r + h_s + gap - min_rb
        bw = max(w_s, w_b)
        start_c = curx
        shift_b_c = start_c - min_cb
        shift_s_c = start_c + (bw - w_s)//2 - min_cs
        for r,c in comp_b:
            out[r+shift_b_r][c+shift_b_c] = v
        for r,c in comp_s:
            out[r+shift_s_r][c+shift_s_c] = v
        curx += bw + 1
    return out