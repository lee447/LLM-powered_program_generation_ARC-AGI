from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c and not seen[y][x]:
                stack = [(y, x)]
                pts = []
                seen[y][x] = True
                while stack:
                    yy, xx = stack.pop()
                    pts.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==c:
                            seen[ny][nx] = True
                            stack.append((ny, nx))
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                miny, maxy = min(ys), max(ys)
                minx, maxx = min(xs), max(xs)
                ph, pw = maxy-miny+1, maxx-minx+1
                mask = {(yy-miny, xx-minx) for yy, xx in pts}
                per = 2*(ph+pw)-4
                shape = 'ring' if len(mask)==per else 'plus'
                comps.append((shape, c, miny, pts, ph, pw, mask))
    rings = sorted([c for c in comps if c[0]=='ring'], key=lambda x:x[2])
    plus = sorted([c for c in comps if c[0]=='plus'], key=lambda x:x[2])
    out = [[0]*w for _ in range(h)]
    x0 = 1
    for _, color, _, _, ph, pw, mask in rings:
        for ry, rx in mask:
            out[ry][x0+rx] = color
        x0 += pw+1
    total_pw = sum(c[5] for c in plus)
    x1 = w - total_pw
    for _, color, _, _, ph, pw, mask in plus:
        y1 = h - ph
        for ry, rx in mask:
            out[y1+ry][x1+rx] = color
        x1 += pw
    return out