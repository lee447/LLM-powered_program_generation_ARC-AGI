from typing import List
from collections import deque, defaultdict

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row]
    bg = max(set(flat), key=flat.count)
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                q = deque([(i, j)])
                vis[i][j] = True
                cells = []
                while q:
                    x, y = q.popleft()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == col:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                rs = [x for x,_ in cells]
                cs = [y for _,y in cells]
                comps.append({
                    'cells': cells,
                    'r1': min(rs), 'r2': max(rs),
                    'c1': min(cs), 'c2': max(cs),
                    'color': col
                })

    # group comps into shapes by overlapping bboxes across colors
    n = len(comps)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in range(n):
        for j in range(i+1, n):
            if comps[i]['color'] != comps[j]['color']:
                if (comps[i]['r1'] <= comps[j]['r2'] and comps[j]['r1'] <= comps[i]['r2']
                and comps[i]['c1'] <= comps[j]['c2'] and comps[j]['c1'] <= comps[i]['c2']):
                    union(i, j)

    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    shapes = list(groups.values())

    axis = 1 if h > w else 0
    centers = []
    for shape in shapes:
        r1 = min(comps[i]['r1'] for i in shape)
        r2 = max(comps[i]['r2'] for i in shape)
        c1 = min(comps[i]['c1'] for i in shape)
        c2 = max(comps[i]['c2'] for i in shape)
        centers.append((r1+r2)//2 if axis == 0 else (c1+c2)//2)

    tgt = sorted(centers)[len(centers)//2]
    out = [[bg]*w for _ in range(h)]
    for shape, ctr in zip(shapes, centers):
        d = tgt - ctr
        for i in shape:
            for x, y in comps[i]['cells']:
                nx, ny = (x+d, y) if axis == 0 else (x, y+d)
                out[nx][ny] = grid[x][y]
    return out