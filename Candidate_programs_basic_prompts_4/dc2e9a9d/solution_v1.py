def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    shapes = []
    for r in range(H):
        for c in range(W):
            if grid[r][c]==3 and not seen[r][c]:
                stack = [(r,c)]
                bbox = [r, r, c, c]
                pts = []
                seen[r][c] = True
                while stack:
                    y,x = stack.pop()
                    pts.append((y,x))
                    bbox[0] = min(bbox[0], y)
                    bbox[1] = max(bbox[1], y)
                    bbox[2] = min(bbox[2], x)
                    bbox[3] = max(bbox[3], x)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and grid[ny][nx]==3 and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((ny,nx))
                shapes.append((bbox, pts))
    def empty_region(r0, c0, h, w):
        if r0<0 or c0<0 or r0+h>H or c0+w>W: return False
        for y in range(r0, r0+h):
            for x in range(c0, c0+w):
                if grid[y][x]!=0: return False
        return True
    for bbox, pts in sorted(shapes, key=lambda b: (b[0][0], b[0][2])):
        y0,y1,x0,x1 = bbox
        h = y1-y0+1
        w = x1-x0+1
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for dy,dx in dirs:
            nr = y0 + dy*(h+1)
            nc = x0 + dx*(w+1)
            if empty_region(nr, nc, h, w):
                col = 1 if dy==0 else 8
                for y,x in pts:
                    yy = nr + (y-y0)
                    xx = nc + (x-x0)
                    grid[yy][xx] = col
                if dy!=0:
                    cy = nr + (h-1 if dy>0 else 0)
                    cx = nc + w//2
                    grid[cy+dy][cx] = col
                break
    return grid