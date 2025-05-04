import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    colors = sorted(set(grid[r][c] for r in range(h) for c in range(w)) & {1,2,3,6})
    occupied = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] in colors:
                res[r][c] = grid[r][c]
                occupied[r][c] = True
    for color in colors:
        pts = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==color]
        if len(pts)==2:
            a, b = pts
        else:
            r,c = pts[0]
            cand = []
            for rr,cc in [(r,0),(r,w-1),(0,c),(h-1,c)]:
                cand.append((abs(rr-r)+abs(cc-c), rr, cc))
            _, rr, cc = min(cand)
            a = (r,c)
            b = (rr,cc)
            res[rr][cc] = color
            occupied[rr][cc] = True
        (r1,c1),(r2,c2) = a,b
        if r1==r2:
            for cc in range(min(c1,c2)+1,max(c1,c2)):
                res[r1][cc]=5
        elif c1==c2:
            for rr in range(min(r1,r2)+1,max(r1,r2)):
                res[rr][c1]=5
        else:
            if not occupied[r1][c2]:
                br,bc = r1,c2
            else:
                br,bc = r2,c1
            res[br][bc]=4
            for rr in range(min(r1,br)+1,max(r1,br)):
                res[rr][c1]=5
            for cc in range(min(c1,bc)+1,max(c1,bc)):
                res[br][cc]=5
            for rr in range(min(br,r2)+1,max(br,r2)):
                res[rr][c2]=5
            for cc in range(min(c2,bc)+1,max(c2,bc)):
                res[br][cc]=5
    return res