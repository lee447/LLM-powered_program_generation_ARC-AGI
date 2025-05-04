from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_clusters(color):
        vis = [[False]*w for _ in range(h)]
        clusters = []
        for i in range(h):
            for j in range(w):
                if grid[i][j] == color and not vis[i][j]:
                    stack = [(i,j)]
                    comp = []
                    vis[i][j] = True
                    while stack:
                        x,y = stack.pop()
                        comp.append((x,y))
                        for dx,dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==color:
                                vis[nx][ny] = True
                                stack.append((nx,ny))
                    clusters.append(comp)
        return clusters
    def canonical(coords):
        pts = coords
        norms = []
        for _ in range(4):
            pts = [(c, -r) for r,c in pts]
            for flip in (False, True):
                arr = [(-r,c) if flip else (r,c) for r,c in pts]
                mr = min(r for r,c in arr); mc = min(c for r,c in arr)
                norm = tuple(sorted((r-mr,c-mc) for r,c in arr))
                norms.append(norm)
        return min(norms)
    cl4 = find_clusters(4)
    cl6 = find_clusters(6)
    shapes = {}
    for comp,color in ((cl4,4),(cl6,6)):
        for c in comp:
            key = canonical(c)
            if key not in shapes: shapes[key]=[]
            shapes[key].append((c,color))
    pattern = max([k for k,v in shapes.items() if len(v)>1], key=lambda k: len(shapes[k]))
    reps = shapes[pattern]
    def anchor_key(item):
        comp,_ = item
        return (min(r for r,c in comp), min(c for r,c in comp))
    anc_comp, anc_col = min(reps, key=anchor_key)
    for comp,col in reps:
        if col != anc_col:
            for r,c in comp:
                grid[r][c] = anc_col
    return grid