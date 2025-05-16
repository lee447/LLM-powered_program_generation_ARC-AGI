from collections import Counter
def solve(grid):
    H, W = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=cnt.get)
    def is_border(c):
        pts = [(r, col) for r in range(H) for col in range(W) if grid[r][col]==c]
        if not pts: return False
        rs = [r for r,_ in pts]; cs = [c0 for _,c0 in pts]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        expected = 2*(r1-r0+1 + c1-c0+1) - 4
        if len(pts)!=expected: return False
        for r,cc in pts:
            if not (r==r0 or r==r1 or cc==c0 or cc==c1):
                return False
        return True
    borders = []
    for c in cnt:
        if c!=bg and is_border(c):
            pts = [(r, col) for r in range(H) for col in range(W) if grid[r][col]==c]
            rs = [r for r,_ in pts]; cs = [c0 for _,c0 in pts]
            area = (max(rs)-min(rs)+1)*(max(cs)-min(cs)+1)
            borders.append((area, c))
    borders.sort()
    _, border = borders[len(borders)//2]
    pts = [(r, col) for r in range(H) for col in range(W) if grid[r][col]==border]
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