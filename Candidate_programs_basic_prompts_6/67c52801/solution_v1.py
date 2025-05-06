from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    bg = None
    counts = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    for color, cnt in counts.items():
        for r in range(H):
            if all(grid[r][c] == color for c in range(W)):
                bg = color
                break
        if bg is not None:
            break
    if bg is None:
        bg = max(counts, key=lambda k: counts[k])
    occ = [[0]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == bg:
                occ[r][c] = bg
    seen = [[False]*W for _ in range(H)]
    shapes = []
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0 and v != bg and not seen[r][c]:
                col = v
                stack = [(r,c)]
                comp = []
                seen[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and grid[nx][ny] == col:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                r0 = min(x for x,y in comp)
                c0 = min(y for x,y in comp)
                r1 = max(x for x,y in comp)
                shapes.append((r1, r0, c0, col, comp))
    shapes.sort(reverse=True)
    for _, r0, c0, col, comp in shapes:
        coords = [(x-r0, y-c0) for x,y in comp]
        h0 = max(x for x,y in coords) - min(x for x,y in coords) + 1
        w0 = max(y for x,y in coords) - min(y for x,y in coords) + 1
        best = None
        for oid in range(4):
            if oid == 0:
                cr = coords; hh, ww = h0, w0
            elif oid == 1:
                cr = [(y, h0-1-x) for x,y in coords]; hh, ww = w0, h0
            elif oid == 2:
                cr = [(h0-1-x, w0-1-y) for x,y in coords]; hh, ww = h0, w0
            else:
                cr = [(w0-1-y, x) for x,y in coords]; hh, ww = w0, h0
            for xoff in range(W-ww+1):
                d = 0
                while True:
                    ok = True
                    for dr,dc in cr:
                        rr = r0 + dr + d
                        cc = xoff + dc
                        if rr+1 >= H or occ[rr+1][cc] != 0:
                            ok = False
                            break
                    if ok:
                        d += 1
                        continue
                    break
                bottom = max(r0+dr+d for dr,dc in cr)
                cand = (bottom, oid, xoff, d, cr)
                if best is None or cand[0] > best[0] or (cand[0]==best[0] and (cand[1]<best[1] or (cand[1]==best[1] and cand[2]<best[2]))):
                    best = cand
        _, oid, xoff, d, cr = best
        for dr,dc in cr:
            occ[r0+dr+d][xoff+dc] = col
    return occ