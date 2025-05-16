from collections import Counter
def solve(grid):
    H, W = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=cnt.get)
    def is_border(color):
        pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c]==color]
        if not pts: return False
        rs = [r for r,_ in pts]; cs = [c0 for _,c0 in pts]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        exp = 2*((r1-r0+1)+(c1-c0+1)) - 4
        if len(pts)!=exp: return False
        for r, c in pts:
            if not (r==r0 or r==r1 or c==c0 or c==c1):
                return False
        return True
    borders = []
    for color in cnt:
        if color!=bg and is_border(color):
            pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c]==color]
            rs = [r for r,_ in pts]; cs = [c0 for _,c0 in pts]
            area = (max(rs)-min(rs)+1)*(max(cs)-min(cs)+1)
            borders.append((area, color))
    borders.sort()
    if len(borders)>2:
        border = borders[1][1]
    else:
        border = borders[0][1]
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c]==border]
    rs = [r for r,_ in pts]; cs = [c0 for _,c0 in pts]
    r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
    h = r1 - r0 - 1; w = c1 - c0 - 1
    fill = grid[r0+1][c0+1]
    out = [[fill]*w for _ in range(h)]
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v==bg or v==border or v==fill: continue
            if r < r0:
                orow = r0-1-r
            elif r > r1:
                orow = r-(r1+1)
            else:
                orow = r-(r0+1)
            if c < c0:
                ocol = c0-1-c
            elif c > c1:
                ocol = c-(c1+1)
            else:
                ocol = c-(c0+1)
            if 0 <= orow < h and 0 <= ocol < w:
                out[orow][ocol] = v
    return out