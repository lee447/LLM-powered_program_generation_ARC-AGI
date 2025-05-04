def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(i, j, grid[i][j]) for i in range(h) for j in range(w) if grid[i][j] not in (0,5)]
    out = [[0]*w for _ in range(h)]
    for i, j, c in pts:
        out[i][j] = c
    def draw(a, b):
        x1,y1,c1 = a; x2,y2,c2 = b
        dx = x2-x1; dy = y2-y1
        sx = 1 if dx>0 else -1
        sy = 1 if dy>0 else -1
        if abs(dx)==abs(dy):
            for k in range(abs(dx)+1):
                xi = x1 + k*sx
                yi = y1 + k*sy
                out[xi][yi] = c1 if k==0 else (c2 if k==abs(dx) else 5)
            for k in range(1, abs(dx)+1):
                xi = x1 + k*sx
                yi = y1
                if 0<=xi<h and 0<=yi<w and out[xi][yi]==0: out[xi][yi] = 5
            for k in range(1, abs(dx)+1):
                xi = x1
                yi = y1 + k*sy
                if 0<=xi<h and 0<=yi<w and out[xi][yi]==0: out[xi][yi] = 5
        else:
            for i in range(min(x1,x2), max(x1,x2)+1):
                if 0<=i<h and 0<=y1<w and out[i][y1]==0: out[i][y1]=5
            for j in range(min(y1,y2), max(y1,y2)+1):
                if 0<=x2<h and 0<=j<w and out[x2][j]==0: out[x2][j]=5
            out[x2][y1] = c1
            out[x1][y2] = c2
    pts_sorted = sorted(pts)
    for a, b in zip(pts_sorted, pts_sorted[1:]):
        draw(a, b)
    return out