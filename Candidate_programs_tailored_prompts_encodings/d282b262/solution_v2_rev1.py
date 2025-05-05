from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                coords = []
                while stack:
                    r,c = stack.pop()
                    coords.append((r,c,grid[r][c]))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                rs = [r for r,_,_ in coords]
                cs = [c for _,c,_ in coords]
                clusters.append({
                    'coords': coords,
                    'min_r': min(rs),
                    'max_r': max(rs),
                    'min_c': min(cs),
                    'max_c': max(cs),
                    'w': max(cs)-min(cs)+1
                })
    clusters.sort(key=lambda c: c['min_r'])
    bands = []
    for c in clusters:
        if not bands or c['min_r'] > bands[-1]['max_r']:
            bands.append({'max_r': c['max_r'], 'cls': [c]})
        else:
            bands[-1]['cls'].append(c)
    out = [[0]*w for _ in range(h)]
    for b in bands:
        b['cls'].sort(key=lambda c: c['min_c'])
        total = sum(c['w'] for c in b['cls'])
        start = w - total
        for c in b['cls']:
            for r, cc, v in c['coords']:
                out[r][start + (cc - c['min_c'])] = v
            start += c['w']
    return out