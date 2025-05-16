from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    blocks = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and not seen[i][j]:
                pts = [(i,j)]
                seen[i][j] = True
                for k in range(len(pts)):
                    y,x = pts[k]
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx]==c:
                            seen[ny][nx] = True
                            pts.append((ny,nx))
                if len(pts)==16:
                    ys = [p[0] for p in pts]
                    xs = [p[1] for p in pts]
                    blocks.append((min(ys),min(xs),grid[i][j]))
    blocks.sort(key=lambda t:(t[0],t[1]))
    n = len(blocks)
    if n==0:
        return []
    C = 2
    R = (n + C - 1)//C
    out = [[0]*(4*C) for _ in range(4*R)]
    for idx,(_,_,c) in enumerate(blocks):
        r, col = divmod(idx, C)
        y0, x0 = 4*r, 4*col
        for dy in range(4):
            for dx in range(4):
                out[y0+dy][x0+dx] = c
    return out