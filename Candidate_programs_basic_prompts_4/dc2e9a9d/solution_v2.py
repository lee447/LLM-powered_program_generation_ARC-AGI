from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    clusters: List[List[Tuple[int,int]]] = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 3 and not seen[y][x]:
                stack = [(y,x)]
                comp = []
                seen[y][x] = True
                while stack:
                    cy, cx = stack.pop()
                    comp.append((cy,cx))
                    for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx]==3 and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((ny,nx))
                clusters.append(comp)
    clusters.sort(key=lambda comp: (min(y for y,x in comp), min(x for y,x in comp)))
    out = [row[:] for row in grid]
    dirs = ['right','down','left','up']
    cols = [1,8]
    for i, comp in enumerate(clusters):
        ymin = min(y for y,x in comp)
        ymax = max(y for y,x in comp)
        xmin = min(x for y,x in comp)
        xmax = max(x for y,x in comp)
        ch = ymax - ymin + 1
        cw = xmax - xmin + 1
        color = cols[i % 2]
        best = None
        best_area = -1
        for d in dirs:
            if d == 'right':
                sx, sy = xmax+1, ymin
                if sx+cw <= w-1:
                    area = (w-1 - sx)*ch
                    fit = True
                    for yy in range(sy, sy+ch):
                        for xx in range(sx+1, sx+1+cw):
                            if yy<0 or yy>=h or xx<0 or xx>=w or grid[yy][xx]!=0:
                                fit = False; break
                        if not fit: break
                    if fit and area > best_area:
                        best_area, best = area, ('right', sx+1, sy)
            if d == 'down':
                sx, sy = xmin, ymax+1
                if sy+ch <= h-1:
                    area = (h-1 - sy)*cw
                    fit = True
                    for yy in range(sy+1, sy+1+ch):
                        for xx in range(sx, sx+cw):
                            if yy<0 or yy>=h or xx<0 or xx>=w or grid[yy][xx]!=0:
                                fit = False; break
                        if not fit: break
                    if fit and area > best_area:
                        best_area, best = area, ('down', sx, sy+1)
            if d == 'left':
                sx, sy = xmin-1, ymin
                if sx-cw >= 0:
                    area = sx * ch
                    fit = True
                    for yy in range(sy, sy+ch):
                        for xx in range(sx- cw +1, sx):
                            if yy<0 or yy>=h or xx<0 or xx>=w or grid[yy][xx]!=0:
                                fit = False; break
                        if not fit: break
                    if fit and area > best_area:
                        best_area, best = area, ('left', sx-cw+1, sy)
            if d == 'up':
                sx, sy = xmin, ymin-1
                if sy-ch >= 0:
                    area = sy * cw
                    fit = True
                    for yy in range(sy - ch +1, sy):
                        for xx in range(sx, sx+cw):
                            if yy<0 or yy>=h or xx<0 or xx>=w or grid[yy][xx]!=0:
                                fit = False; break
                        if not fit: break
                    if fit and area > best_area:
                        best_area, best = area, ('up', sx, sy-ch+1)
        if best:
            d, bx, by = best
            for dy in range(ch):
                for dx in range(cw):
                    out[by+dy][bx+dx] = color
    return out