from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not seen[y][x]:
                q = deque([(y,x)])
                seen[y][x] = True
                coords = []
                min_x = w; max_x = -1; min_y = h; max_y = -1
                while q:
                    cy, cx = q.popleft()
                    coords.append((cy,cx))
                    if cx<min_x: min_x = cx
                    if cx>max_x: max_x = cx
                    if cy<min_y: min_y = cy
                    if cy>max_y: max_y = cy
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and grid[ny][nx]!=0 and not seen[ny][nx]:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                clusters.append({
                    'coords': coords,
                    'min_x': min_x,
                    'max_x': max_x,
                    'min_y': min_y,
                    'max_y': max_y,
                    'width': max_x-min_x+1
                })
    clusters.sort(key=lambda c:(-c['min_x'], c['min_y']))
    assigned = []
    for c in clusters:
        x_new = w - c['width']
        for d in assigned:
            if not (c['max_y'] < d['min_y'] or c['min_y'] > d['max_y']):
                x_new = min(x_new, d['x_new'] - c['width'])
        c['x_new'] = x_new
        assigned.append(c)
    out = [[0]*w for _ in range(h)]
    for c in clusters:
        dx0 = c['min_x']
        for y,x in c['coords']:
            out[y][c['x_new'] + (x-dx0)] = grid[y][x]
    return out