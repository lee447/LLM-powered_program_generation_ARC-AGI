from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    regions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                visited[i][j] = True
                pts = []
                while stack:
                    y,x = stack.pop()
                    pts.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx] = True
                            stack.append((ny,nx))
                minr = min(y for y,x in pts)
                maxr = max(y for y,x in pts)
                minc = min(x for y,x in pts)
                maxc = max(x for y,x in pts)
                regions.append({
                    'color': col,
                    'pixels': pts,
                    'minr': minr, 'maxr': maxr,
                    'minc': minc, 'maxc': maxc
                })
    seq = sorted(regions, key=lambda r: (r['minr'], r['minc']))
    for idx, r in enumerate(seq):
        if idx == 0 or idx == len(seq)-1:
            r['cur_pixels'] = list(r['pixels'])
            r['cur_minr'] = r['minr']
            r['cur_maxr'] = r['maxr']
            r['cur_minc'] = r['minc']
            r['cur_maxc'] = r['maxc']
        else:
            prev = seq[idx-1]
            dx = dy = 0
            if r['minr'] <= prev['cur_maxr'] and r['maxr'] >= prev['cur_minr']:
                dx = prev['cur_maxc'] - r['minc']
                if dx < 0: dx = 0
            elif r['minc'] <= prev['cur_maxc'] and r['maxc'] >= prev['cur_minc']:
                dy = prev['cur_maxr'] - r['minr']
                if dy < 0: dy = 0
            new_pixels = [(y+dy, x+dx) for y,x in r['pixels']]
            minr = min(y for y,x in new_pixels)
            maxr = max(y for y,x in new_pixels)
            minc = min(x for y,x in new_pixels)
            maxc = max(x for y,x in new_pixels)
            r['cur_pixels'] = new_pixels
            r['cur_minr'] = minr
            r['cur_maxr'] = maxr
            r['cur_minc'] = minc
            r['cur_maxc'] = maxc
    out = [[0]*w for _ in range(h)]
    for r in seq:
        for y,x in r['cur_pixels']:
            out[y][x] = r['color']
    return out