def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    regions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                pixels = []
                while stack:
                    y, x = stack.pop()
                    pixels.append((y, x))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == color:
                            visited[ny][nx] = True
                            stack.append((ny, nx))
                minr = min(y for y, x in pixels)
                maxr = max(y for y, x in pixels)
                minc = min(x for y, x in pixels)
                maxc = max(x for y, x in pixels)
                regions.append({
                    'color': color,
                    'pixels': pixels,
                    'minr': minr, 'maxr': maxr,
                    'minc': minc, 'maxc': maxc
                })
    pink = next(r for r in regions if r['color'] == 6)
    green = next(r for r in regions if r['color'] == 3)
    others = [r for r in regions if r['color'] not in (6, 3)]
    others_sorted = sorted(others, key=lambda r: r['minr'])
    seq = [pink] + others_sorted + [green]
    for r in seq:
        r['cur_pixels'] = list(r['pixels'])
        r['cur_minr'] = r['minr']
        r['cur_maxr'] = r['maxr']
        r['cur_minc'] = r['minc']
        r['cur_maxc'] = r['maxc']
    placed = [seq[0]]
    for idx, r in enumerate(seq[1:], 1):
        if r['color'] == 3:
            placed.append(r)
            continue
        prev = placed[-1]
        if (idx-1) % 2 == 0:
            dx = prev['cur_maxc'] - r['cur_minc']
            dy = 0
        else:
            dy = prev['cur_maxr'] - r['cur_minr']
            dx = 0
        new_pixels = [(y+dy, x+dx) for y, x in r['pixels']]
        r['cur_pixels'] = new_pixels
        r['cur_minr'] = min(y for y, x in new_pixels)
        r['cur_maxr'] = max(y for y, x in new_pixels)
        r['cur_minc'] = min(x for y, x in new_pixels)
        r['cur_maxc'] = max(x for y, x in new_pixels)
        placed.append(r)
    out = [[0]*w for _ in range(h)]
    for r in seq:
        for y, x in r['cur_pixels']:
            out[y][x] = r['color']
    return out