def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    patches_by_color = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v and not seen[r][c]:
                q = [(r,c)]
                seen[r][c] = True
                cells = []
                mr = r
                mc = c
                for x,y in q:
                    cells.append((x,y))
                    mr = min(mr, x)
                    mc = min(mc, y)
                    for dr,dc in dirs:
                        nr, nc = x+dr, y+dc
                        if 0<=nr<H and 0<=nc<W and not seen[nr][nc] and grid[nr][nc]==v:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                patches_by_color.setdefault(v, []).append((mr, len(cells), cells))
    colors = sorted(patches_by_color)
    lo, hi = colors[0], colors[1]
    out = [[0]*W for _ in range(H)]
    half = H//2
    def place(color, start_c):
        pats = sorted(patches_by_color[color], key=lambda x: x[0])
        r = half
        for _, cnt, _ in pats:
            s = int(cnt**0.5)
            if s*s==cnt:
                h = w = s
            else:
                h, w = 1, cnt
            if r+h>H: break
            for dr in range(h):
                for dc in range(w):
                    out[r+dr][start_c+dc] = color
            r += h+1
    place(lo, 0)
    max_w_lo = max(int(sz**0.5)**2==sz and int(sz**0.5) or sz for _,sz,_ in patches_by_color[lo])
    gap = 1
    place(hi, max_w_lo+gap)
    return out